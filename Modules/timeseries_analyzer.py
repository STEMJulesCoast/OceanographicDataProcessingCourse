import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import detrend
from scipy.stats import linregress, chi2
import pycwt as wavelet
from numpy.fft import fft, fftfreq

class TimeSeriesAnalyzer:
    """
    A class to analyze time series data, perform climatology computations, 
    detrend anomalies, and conduct Fourier and wavelet analyses for selected regions. 
    
    Note: This class currently supports only time series with monthly or daily resolution. 
    For data with other temporal resolutions, the class needs to be extended and adjusted accordingly.

    Attributes:
    -----------
    _dataset : xarray.Dataset
        The input dataset containing the time series data for analysis.
    _ds_anom_detrended : xarray.Dataset
        The dataset storing the detrended anomalies after computation.
    _climatology : xarray.Dataset
        The dataset storing the climatology (mean for each time period).
    _annual_amplitude : xarray.Dataset
        The dataset storing the annual amplitude for each variable.

    Methods:
    --------
    compute_climatology():
        Computes the climatology (mean for each month or day of the year) 
        based on the detected time resolution (daily or monthly).
    compute_anomalies_and_detrend():
        Computes the climatology, anomalies, and detrends the anomalies 
        for all variables in the dataset.
    compute_annual_amplitude():
        Calculates the annual amplitude for all variables in the dataset 
        based on the climatology.
    plot_std_and_annual_var(variable, vmin=0, vmax=10, cmap='plasma', background='white'):
        Plots the standard deviation of the original data and the annual variability.
    save_results(filepath):
        Saves the detrended anomaly dataset to a NetCDF file.
    filter_and_analyze_cycle(variable, vmin=0, vmax=2, window_size=15, cmap='plasma', background='white'):
        Applies a low-pass and high-pass filter to the data and visualizes the variability.
    compute_fft(variable, lon_min, lon_max, lat_min, lat_max, use_detrended=True, time_start=None, time_end=None):
        Performs a Fourier Transform on the selected variable over the specified region 
        and identifies significant periods.
    wavelet_analysis(variable, lon_min, lon_max, lat_min, lat_max, use_detrended=True, dt=1):
        Performs a wavelet analysis using the Morlet wavelet on the selected variable 
        over the specified region, displaying the wavelet power spectrum and global power spectrum.
    """
    def __init__(self, dataset):
        """
        Initializes the TimeSeriesAnalyzer with the dataset.
        Stores the detrended anomalies and climatology in separate xarray.Datasets.
        """
        self._dataset = dataset
        self._ds_anom_detrended = xr.Dataset()
        self._climatology = xr.Dataset()
        self._annual_amplitude = xr.Dataset()

    @property
    def dataset(self):
        """Getter for the dataset."""
        return self._dataset

    @dataset.setter
    def dataset(self, value):
        """Setter for the dataset, ensures the value is an xarray.Dataset."""
        if not isinstance(value, xr.Dataset):
            raise ValueError("Dataset must be an instance of xarray.Dataset.")
        self._dataset = value

    @property
    def ds_anom_detrended(self):
        """Getter for the detrended anomaly dataset."""
        return self._ds_anom_detrended

    @property
    def climatology(self):
        """Getter for the climatology dataset."""
        return self._climatology

    def _get_time_resolution(self):
        """
        Determines the time resolution of the dataset by examining the difference between time steps.
        Returns the frequency in days (e.g., 1 for daily, 30 for monthly).
        """
        # Calculate the difference between consecutive time steps
        time_diff = np.diff(self._dataset['time'].values).astype('timedelta64[D]').astype(int)

        # Calculate the mean time difference
        avg_diff = np.mean(time_diff)

        # If the average time difference is close to 30 days, assume monthly data
        if avg_diff < 2:
            return 1  # Daily data
        elif avg_diff < 32:
            return 30  # Monthly data
        else:
            raise ValueError("Unsupported time resolution. Please check the dataset.")


    def compute_climatology(self):
        """
        Computes the climatology (mean for each month or day of the year) based on the time resolution.
        Automatically detects whether the data is daily or monthly.
        """
        time_res = self._get_time_resolution()

        for var in self._dataset.data_vars:
            if time_res == 1:
                # Daily data: calculate climatology for each day of the year
                climatology = self._dataset[var].groupby('time.dayofyear').mean('time')
            elif time_res >= 28:
                # Monthly data: calculate climatology for each month
                climatology = self._dataset[var].groupby('time.month').mean('time')
            else:
                raise ValueError("Unsupported time resolution.")
            
            # Store the climatology for future use
            self._climatology[var] = climatology
        return self._climatology

    def compute_anomalies_and_detrend(self):
        """
        Computes the monthly climatology, anomalies, and detrends the anomalies.
        Handles both 3D and 4D datasets by automatically determining the dimensions.
        """
        # Ensure climatology is computed for all variables
        self.compute_climatology()

        for var in self._dataset.data_vars:
            dims = self._dataset[var].dims

            # Calculate climatology based on time resolution (daily or monthly)
            time_res = self._get_time_resolution()
            # Retrieve precomputed climatology
            climatology = self._climatology[var]

            if time_res == 1:
                # Daily
                anomalies = self._dataset[var].groupby('time.dayofyear') - climatology
            elif time_res >= 28:
                # Monthly
                anomalies = self._dataset[var].groupby('time.month') - climatology


            # Detrend the anomalies along the time axis
            detrended_anomalies = xr.apply_ufunc(
                detrend, anomalies.fillna(0),
                input_core_dims=[['time']], output_core_dims=[['time']],
                dask='allowed'
            ).where(~anomalies.isnull())  # Reapply the NaN mask

            # Automatically transpose dimensions based on detected shape
            transpose_dims = ['time'] + [dim for dim in dims if dim not in ['time']]
            self._ds_anom_detrended[var] = detrended_anomalies.transpose(*transpose_dims)

            # Copy attributes and add long_name if available
            self._ds_anom_detrended[var].attrs = self._dataset[var].attrs
            if 'long_name' in self._dataset[var].attrs:
                self._ds_anom_detrended[var].attrs['long_name'] = f"Detrended anomaly of {self._dataset[var].attrs['long_name']}"

        # Add description to the detrended dataset
        self._ds_anom_detrended.attrs['description'] = 'Detrended anomalies of all variables.'
        ds_anom = self._ds_anom_detrended
        return ds_anom

    def compute_annual_amplitude(self):
        """
        Computes the annual amplitude for all variables in the dataset based on the climatology.
        Stores the result in self._annual_amplitude as an xarray.Dataset.
        """
        for var in self._climatology.data_vars:
            time_res = self._get_time_resolution()

            if time_res == 1:
                # Daily data: Calculate annual variability based on day-of-year climatology
                max_clim = self._climatology[var].max(dim='dayofyear')
                min_clim = self._climatology[var].min(dim='dayofyear')
            elif time_res >= 28:
                # Monthly data: Calculate annual variability based on monthly climatology
                max_clim = self._climatology[var].max(dim='month')
                min_clim = self._climatology[var].min(dim='month')
            else:
                raise ValueError("Unsupported time resolution.")

            # Compute annual amplitude and store in xarray.Dataset
            self._annual_amplitude[var] = (max_clim - min_clim)/2
        return self._annual_amplitude
    
    def plot_std_and_annual_var(self,variable, vmin=0, vmax=10, cmap='plasma', background='white'):

        # Ensure climatology is computed for the specific variable
        if self._climatology is None or variable not in self._climatology:
            print(f"Climatology for {variable} not found. Computing climatology first.")
            self.compute_climatology()
        
        original_std = self._dataset[variable].std(dim='time')
        annual_var = self._climatology[variable].std(dim='month' if 'month' in self._climatology[variable].dims else 'dayofyear')
        # Plotting Setup
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5), facecolor=background)
        fig.subplots_adjust(hspace=0.5, wspace=0.5)

        # Standard deviations and annual variability plots
        plots = [original_std, annual_var]
        titles = ['Variability (Std)', 'Annual Variability (Std)']

        for ax, data, title in zip(axes.flatten(), plots, titles):
            data.plot(ax=ax, vmin=vmin, vmax=vmax, cmap=cmap)
            ax.set_title(title)

        

        plt.show()

    

    def save_results(self, filepath):
        """
        Saves the detrended anomaly dataset to a NetCDF file.
        """
        self._ds_anom_detrended.to_netcdf(filepath, engine='h5netcdf', compute=True)

    def filter_and_analyze_cycle(self, variable, vmin=0, vmax=2, window_size=15, cmap='plasma', background='white'):
        """
        Filters and analyzes the data by computing low-pass and high-pass components and visualizing them.
        Also retrieves or calculates the annual variability from the climatology.
        """
        # Check if detrended anomalies for the specific variable have been calculated
        if self._ds_anom_detrended is None or variable not in self._ds_anom_detrended:
            # Compute anomalies and detrend them if they don't exist yet
            print(f"Detrended anomalies for {variable} not found. Computing anomalies and detrending the data.")
            self.compute_anomalies_and_detrend()

        # Check if 'depth' exists in the dataset
        if 'depth' in self._ds_anom_detrended[variable].dims:
            # If 'depth' exists, select the surface layer
            clean_data = self._ds_anom_detrended[variable].isel(depth=0).dropna(dim='time', how='all')
        else:   
            # If 'depth' does not exist, use the variable as is
            clean_data = self._ds_anom_detrended[variable].dropna(dim='time', how='all')
            
        # Low-Pass Filter to remove high frequency variations
        low_pass = clean_data.rolling(time=window_size, center=True).mean()

        # High-Pass Filter: difference of anomalies and low_pass to get higher frequency variations
        high_pass = clean_data - low_pass


        # Plotting Setup
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10), facecolor=background)
        fig.subplots_adjust(hspace=0.5, wspace=0.5)

        # Standard deviations and annual variability plots
        plots = [clean_data.std(dim='time'), low_pass.std(dim='time'), high_pass.std(dim='time')]
        titles = ['Variability of Anomalies (Std)', 'Low-Pass Variability (Std)', 'High-Pass Variability (Std)']

        for ax, data, title in zip(axes.flatten(), plots, titles):
            data.plot(ax=ax, vmin=vmin, vmax=vmax, cmap=cmap)
            ax.set_title(title)

        axes[1, 1].axis('off')  
        plt.show()




    def compute_fft(self, variable, lon_min, lon_max, lat_min, lat_max, use_detrended=True, time_start=None, time_end=None):
        """
        Computes the FFT for a given variable over a specified spatial box and time range.
        Automatically detects coordinate names (e.g., 'longitude' instead of 'lon').
        """
        # Check if detrended anomalies for the specific variable have been calculated
        if use_detrended and (self._ds_anom_detrended is None or variable not in self._ds_anom_detrended):
            # Compute anomalies and detrend them if they don't exist yet
            print(f"Detrended anomalies for {variable} not found. Computing anomalies and detrending the data.")
            self.compute_anomalies_and_detrend()

        # Choose dataset based on `use_detrended`
        data_source = self._ds_anom_detrended if use_detrended else self._dataset
        

        # Automatically detect coordinate names for lon and lat
        lon_name = next((coord for coord in data_source.coords if 'lon' in coord or 'longitude' in coord), None)
        lat_name = next((coord for coord in data_source.coords if 'lat' in coord or 'latitude' in coord), None)

        if lon_name is None or lat_name is None:
            raise ValueError("Longitude or latitude coordinate not found in the dataset.")

        # Select the time range if provided
        if time_start is not None:
            ds_sliced = data_source.sel(time=slice(time_start, time_end))
        else:
            ds_sliced = data_source
        # Select spatial box and compute the mean
        if 'depth' in ds_sliced[variable].dims:
            data_box_mean = ds_sliced[variable].isel(depth=0).sel({lon_name: slice(lon_min, lon_max), lat_name: slice(lat_min, lat_max)}).mean(dim=[lon_name, lat_name])
        else:
            data_box_mean = ds_sliced[variable].sel({lon_name: slice(lon_min, lon_max), lat_name: slice(lat_min, lat_max)}).mean(dim=[lon_name, lat_name])

        
        
        # Apply FFT
        n = len(data_box_mean)
        fft_ds = fft(data_box_mean)
        freq = np.fft.fftfreq(n, d=1)
        periods = np.where(freq != 0, 1 / freq, np.inf)
        
        # Compute power spectrum
        
        power_spec = np.abs(fft_ds) ** 2

        # Identify significant periods
        threshold = np.mean(power_spec) + 2 * np.std(power_spec)
        valid_periods = periods[:n // 2] > 0
        significant_indices = np.where(power_spec[:n // 2][valid_periods] > threshold)[0]
        significant_periods = periods[:n // 2][valid_periods][significant_indices]
        significant_periods = significant_periods[significant_periods < n]
        significant_periods = significant_periods[np.isfinite(significant_periods)]

        print("Significant Periods (in time units)", variable, ":", significant_periods)

    def wavelet_analysis(self, variable, lon_min, lon_max, lat_min, lat_max, use_detrended=True, dt=1):
        """
        Performs wavelet analysis using pycwt on the selected variable.
        """
        # Check if detrended anomalies for the specific variable have been calculated
        if use_detrended and (self._ds_anom_detrended is None or variable not in self._ds_anom_detrended):
            # Compute anomalies and detrend them if they don't exist yet
            print(f"Detrended anomalies for {variable} not found. Computing anomalies and detrending the data.")
            self.compute_anomalies_and_detrend()

        # Choose dataset based on `use_detrended`
        data_source = self._ds_anom_detrended if use_detrended else self._dataset

        # Automatically detect coordinate names for lon and lat
        lon_name = next((coord for coord in data_source.coords if 'lon' in coord or 'longitude' in coord), None)
        lat_name = next((coord for coord in data_source.coords if 'lat' in coord or 'latitude' in coord), None)

        if lon_name is None or lat_name is None:
            raise ValueError("Longitude or latitude coordinate not found in the dataset.")

         # Select spatial box and compute the mean
        if 'depth' in data_source[variable].dims:
            data_box_mean = data_source[variable].isel(depth=0).sel({lon_name: slice(lon_min, lon_max), lat_name: slice(lat_min, lat_max)}).mean(dim=[lon_name, lat_name])
        else:
            data_box_mean = data_source[variable].sel({lon_name: slice(lon_min, lon_max), lat_name: slice(lat_min, lat_max)}).mean(dim=[lon_name, lat_name])

        time = np.arange(len(data_box_mean))
        # Extracting the start and end year from the time coordinate
        start_year = data_box_mean['time'].dt.year[0].item()  # First year in the dataset
        end_year = data_box_mean['time'].dt.year[-1].item()  # Last year in the dataset

        # Length of data_box_mean (number of months)
        num_months = len(data_box_mean['time'])

        # Generate a linspace-like array for the years based on the number of months
        years = np.linspace(start_year, end_year, num=num_months)
        dt = 1
    

        # Calculate the wavelet transform using pycwt
        mother = wavelet.Morlet(6)  # Using the Morlet wavelet
        wave, scales, freqs, coi, fft, fftfreqs = wavelet.cwt(data_box_mean.values,dt, wavelet=mother)

        wave = wave[:, :len(time)] 
        # Manually calculate significance using chi-square distribution
        alpha = 0.05
        dof = 2  # Degrees of freedom for Morlet wavelet
        power = np.abs(wave) ** 2
        signif_level = power.mean() * chi2.ppf(1 - alpha, dof) / dof
        signif = power / signif_level

        periods = 1/freqs

        # Global power spectrum (mean across time)
        global_power = np.mean(power, axis=1)

        
        # Dynamically determine min and max periods based on data
        min_period = 1  # Minimum period in months
        max_period = np.max(periods)  # Maximum period based on the data

        valid_periods = (periods >= min_period) & (periods <= max_period)
        periods = periods[valid_periods]
        wave = wave[valid_periods, :]
        global_power = global_power[valid_periods]
        

        # Dynamically set the yticks based on the available period range
        yticks = np.array([2, 6, 12, 24, 48, 96, 144, 200])
        yticks = yticks[yticks <= max_period]  # Filter out ticks greater than the maximum period in data
        yticklabels = [str(tick) for tick in yticks]  # Labels as strings

        # Plotting
        fig, ax = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [4, 1]})

        # Wavelet Power Spectrum
        c = ax[0].contourf(years, periods, np.abs(wave), levels=39, extend='both', cmap='jet')
        fig.colorbar(c, ax=ax[0], label='Wavelet Power')
        ax[0].set_yscale('log')
        ax[0].set_ylim(min(yticks),max(yticks))
        ax[0].set_yticks(yticks)
        ax[0].set_yticklabels(yticklabels)
        
        ax[0].set_ylabel('Period (Months)')
        ax[0].set_xlabel('Year')
        ax[0].set_title(f'Wavelet Power Spectrum of {variable}')

        
        # Cone of Influence (COI)
        ax[0].fill_between(years, coi, 1/freqs[-1], color='white', alpha=0.3)

        # Significance contours
        ax[0].contour(years, periods, signif, levels=[1.0], colors='white', linewidths=2)

        # Global Power Spectrum
        
        ax[1].plot(global_power, periods, 'b')
        ax[1].set_yscale('log')
        ax[1].set_yticks(yticks)
        ax[1].set_yticklabels(yticklabels)
        ax[1].set_xlabel('Power')
        ax[1].set_title('Global Power Spectrum')
        ax[1].set_ylim(ax[0].get_ylim())
        # Plot Significance Level for Global Power Spectrum
        plt.tight_layout()
        plt.show()


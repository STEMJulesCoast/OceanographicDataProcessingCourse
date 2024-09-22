from scipy.stats import linregress
import xarray as xr
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.ticker import MaxNLocator



def calc_trend(y):
    """
    Calculates the linear trend (slope) for a time series.
    Multiplies the slope by 10 to convert from Unit/year to Unit/decade.
    """
    # Assuming y is a numpy array with no missing values, evenly spaced in time (e.g. monthly data)
    x = np.arange(len(y))
    # Apply linear regression
    slope = linregress(x, y).slope
    # Multiply by 120 to convert from per year to per decade
    return slope * 120

def calculate_trend_per_decade(data):
    """
    Apply the calc_trend function to each grid cell to calculate trend per decade.
    
    Parameters:
    - data: xarray.DataArray with variable values.
    
    Returns:
    - trend_decade: xarray.DataArray with variable trend per decade for each grid cell.
    """
    trend_decade = xr.apply_ufunc(
        calc_trend,
        data,
        vectorize=True,
        input_core_dims=[['time']],  # Time is the core dimension
        dask='allowed'  # Allow Dask for parallel computation
    )
    return trend_decade



def plot_trend(trend_decade, vmin=-0.5, vmax=0.5):
    """
    Plot the trend per grid cell using xarray and matplotlib (no Basemap).
    
    Parameters:
    - trend_decade: xarray.DataArray with SST trend per decade.
    - vmin: Minimum value for colorbar (default is -0.5).
    - vmax: Maximum value for colorbar (default is 0.5).
    """
    # Create symmetrical contour levels centered around zero
    trend_levels = MaxNLocator(nbins=21).tick_values(vmin, vmax)

    # Create a figure for the plot
    fig, ax = plt.subplots(figsize=(12, 7))

    # Plot the trend data using xarray's built-in plotting method
    cf = trend_decade.plot.contourf(ax=ax, levels=trend_levels, cmap='RdBu_r', vmin=vmin, vmax=vmax, 
                                    extend='neither', cbar_kwargs={'label': '°C/decade'})


    # Set titles and labels
    plt.title('Trend of SST per Grid Cell per Decade (°C/decade)')
    
    # Adjust layout for better readability
    plt.tight_layout()
    #plt.savefig("trend.png", transparent=True)
    # Show the plot
    plt.show()


def adjust_longitude(data_array, central_lon):
    """
    Adjusts the longitude to center around 180°.
    """
    if central_lon not in [0, 180]:
        raise ValueError("central_lon must be either 0 or 180.")
    
    data_array = data_array.copy()  # Create a copy to avoid modifying the original data
    lon = data_array['lon']

    if central_lon == 0:
        # Adjust longitudes to be in the range -180° to 180°
        data_array['lon'] = np.where(lon > 180, lon - 360, lon)
    elif central_lon == 180:
        # Adjust longitudes to be in the range 0° to 360°
        data_array['lon'] = np.where(lon < 0, lon + 360, lon)

    #data_array['lon'] = np.where(data_array['lon'] < 0, data_array['lon'] + 360, data_array['lon'])
    return data_array.sortby('lon')  # Sort the longitude after adjusting

def plot_trend_with_basemap(trend_decade, vmin=-0.5, vmax=0.5, variable = 'SST', central_lon=180,label = '°C'):
    """
    Plot the  trend per grid cell using Basemap with 180° as the central longitude.
    
    Parameters:
    - trend_decade: xarray.DataArray with  trend per decade.
    - vmin: Minimum value for colorbar (default is -0.5).
    - vmax: Maximum value for colorbar (default is 0.5).
    """
    # Adjust longitude for 180° as central
    trend_decade = adjust_longitude(trend_decade, central_lon)

    # Create symmetrical contour levels centered around zero
    trend_levels = MaxNLocator(nbins=21).tick_values(vmin, vmax)

    # Generate the meshgrid for contouring
    lons, lats = np.meshgrid(trend_decade.lon, trend_decade.lat)

    # Create a figure with Basemap (Robinson projection, centered at 180°)
    fig, ax = plt.subplots(figsize=(12, 7))

    # Define the map projection using Robinson with 180° central longitude
    m = Basemap(projection='robin', lon_0=central_lon, ax=ax)  # Central longitude set to 180°

    # Transform coordinates into the projection
    x, y = m(lons, lats)

    # Plot the trend data using contourf
    cf = m.contourf(x, y, trend_decade, levels=trend_levels, cmap='RdBu_r', extend='neither')

    # Add coastlines for context
    m.drawcoastlines()

    # Fill continents for better visibility
    m.fillcontinents(color='white', lake_color='lightblue')

    # Add gridlines for orientation
    m.drawparallels(np.arange(-90., 91., 30.), labels=[1, 0, 0, 0], linewidth=0.5, color='gray')
    m.drawmeridians(np.arange(0., 361., 60.), labels=[0, 0, 0, 1], linewidth=0.5, color='gray')

    # Add contour lines to make the levels stand out
    contour_lines = m.contour(x, y, trend_decade, levels=trend_levels, colors='grey', linewidths=0.5)
    plt.clabel(contour_lines, inline=True, fontsize=8, fmt='%1.2f')

    # Plot the colorbar
    cbar = m.colorbar(cf, location='right', pad="10%", aspect=40)
    cbar.set_label(f'{label}/decade')
    cbar.ax.yaxis.set_major_locator(MaxNLocator(nbins=7))

    # Add a title to the plot
    plt.title(f'Trend of {variable} per Grid Cell per Decade ({label}/decade)')
    #plt.savefig("trend.png", transparent=True)
    # Show the plot
    plt.show()
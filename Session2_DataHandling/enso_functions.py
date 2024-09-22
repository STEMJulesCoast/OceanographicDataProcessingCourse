
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def calculate_nino34_index(sst_anom_detrended):
    """
    Calculate the Niño3.4 index based on the detrended SST anomalies.
    """
    # Select the Niño3.4 region (5°S–5°N, 170°W–120°W) when lon = 0:360°S
    sst_anom_nino34 = sst_anom_detrended.sel(lat=slice(5, -5), lon=slice(190, 240))  # Nino3.4 Region
    
    # Calculate the mean SST anomaly in the Niño3.4 region
    sst_anom_nino34_mean = sst_anom_nino34.mean(dim=('lon', 'lat'))
    
    # Compute the Niño3.4 index by applying a 5-month rolling mean
    nino34_index = sst_anom_nino34_mean.rolling(time=5, center=True).mean()  # 5-month rolling mean
    
    return nino34_index

def calculate_composites(anom_detrended, nino34_index):
    """
    Calculate composites for positive and negative ENSO events.
    """
    # Identify positive ENSO events (El Niño): when Niño3.4 index > 0.4 for 6 consecutive months
    positive_nino = ((nino34_index > 0.4).astype('b').rolling(time=6, center=True).sum() >= 6)
    
    # Calculate the average SST anomaly during positive events
    anom_positive = anom_detrended.where(positive_nino).mean(dim='time')

    # Identify negative ENSO events (La Niña): when Niño3.4 index < -0.4 for 6 consecutive months
    negative_nino = ((nino34_index < -0.4).astype('b').rolling(time=6, center=True).sum() >= 6)
    
    # Calculate the average SST anomaly during negative events
    anom_negative = anom_detrended.where(negative_nino).mean(dim='time')

    return anom_positive, anom_negative

def plot_composites(anom_positive, anom_negative, vmin=-1.5, vmax=1.5,label ='°C',variable = 'SST'):
    """
    Plot composites for positive and negative ENSO events.
    """
   

    # Create a figure with two subplots (1x2 layout)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 5), sharey=True)

    # Plot the positive SST anomalies (El Niño events) on the first subplot
    anom_positive.plot(ax=axes[0], cbar_kwargs={'label': label}, vmin=vmin, vmax=vmax, cmap='RdBu_r')
    axes[0].set_title(f'{variable} Anomaly - Positive Niño3.4 (El Niño)')

    # Plot the negative SST anomalies (La Niña events) on the second subplot
    anom_negative.plot(ax=axes[1], cbar_kwargs={'label': label}, vmin=vmin, vmax=vmax, cmap='RdBu_r')
    axes[1].set_title(f'{variable} Anomaly - Negative Niño3.4 (La Niña)')

    # Adjust layout for better readability
    plt.tight_layout()
    
    # Display the plots
    plt.show()

def plot_sst_composites_robinson(sst_anom_positive, sst_anom_negative):
    """
    Plot SST composites for positive and negative ENSO events using Robinson projection.
    """
    # Define colorbar limits
    vmin = -1.5  # Minimum value for colorbar
    vmax = 1.5  # Maximum value for colorbar

    # Create a figure with two subplots (1x2 layout)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7), sharey=True)

    # Create meshgrids for latitude and longitude
    lon2d, lat2d = np.meshgrid(sst_anom_positive.lon, sst_anom_positive.lat)

    # Plot the positive SST anomalies (El Niño) with Robinson projection
    m1 = Basemap(projection='robin', lon_0=180, ax=axes[0])
    x1, y1 = m1(lon2d, lat2d)
    cs1 = m1.contourf(x1, y1, sst_anom_positive, vmin=vmin, vmax=vmax, cmap='RdBu_r')
    m1.drawcoastlines()
    m1.fillcontinents(color='white', lake_color='lightblue')
    m1.drawparallels(np.arange(-90., 91., 30.), labels=[1, 0, 0, 0], linewidth=0.5, color='gray')
    m1.drawmeridians(np.arange(-180., 181., 60.), labels=[0, 0, 0, 1], linewidth=0.5, color='gray')
    axes[0].set_title('SST Anomaly - Positive Niño3.4 (El Niño)')

    # Plot the negative SST anomalies (La Niña) with Robinson projection
    m2 = Basemap(projection='robin', lon_0=0, ax=axes[1])
    x2, y2 = m2(lon2d, lat2d)
    cs2 = m2.contourf(x2, y2, sst_anom_negative, vmin=vmin, vmax=vmax, cmap='RdBu_r')
    m2.drawcoastlines()
    m2.fillcontinents(color='white', lake_color='lightblue')
    m2.drawparallels(np.arange(-90., 91., 30.), labels=[1, 0, 0, 0], linewidth=0.5, color='gray')
    m2.drawmeridians(np.arange(-180., 181., 60.), labels=[0, 0, 0, 1], linewidth=0.5, color='gray')
    axes[1].set_title('SST Anomaly - Negative Niño3.4 (La Niña)')

    # Add a colorbar
    fig.colorbar(cs2, ax=axes.ravel().tolist(), orientation='horizontal', pad=0.05, aspect=50, label='°C')

    # Adjust layout for better readability
    plt.tight_layout()
    
    # Display the plots
    plt.show()

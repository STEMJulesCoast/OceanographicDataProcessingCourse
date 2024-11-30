import numpy as np
import xarray as xr


def compute_windstress(u, v, rho_air=1.293, Cd=1.3e-3):
    """
    Compute wind stress components using 3D xarray DataArrays (e.g., time, lat, lon).
    
    Parameters:
    - u, v: Wind velocity components in m/s (3D xarray.DataArray, e.g., time, lat, lon).
    - rho_air: Air density in kg/m^3. Default is 1.293 kg/m^3.
    - Cd: Drag coefficient. Default is 1.3e-3.
    
    Returns:
    - tau_u, tau_v: Wind stress components in N/m^2 (3D xarray.DataArray).
    """
    
    # Magnitude of wind speed (broadcasting across all dimensions, including time)
    magnitude = np.sqrt(u**2 + v**2)
    
    # Components of wind stress (calculated element-wise over all dimensions)
    tau_u = rho_air * Cd * u * magnitude  # N/m^2
    tau_v = rho_air * Cd * v * magnitude  # N/m^2
    
    return tau_u, tau_v




def compute_windstress_curl(tau_u, tau_v):
    """
    Compute the curl of wind stress using 3D xarray DataArrays.
    
    Parameters:
    - tau_u, tau_v: Wind stress components in N/m^2 (3D xarray.DataArray, e.g., time, lat, lon).
    
    Returns:
    - curl_tau: Curl of wind stress in N/m^3 (3D xarray.DataArray).
    """
    # Automatically detect the dimension names for latitude and longitude
    lat_dim = [dim for dim in tau_u.dims if 'lat' in dim or 'latitude' in dim][0]
    lon_dim = [dim for dim in tau_u.dims if 'lon' in dim or 'longitude' in dim][0]
    
    # Calculate delta based on the resolution of the dataset (assumed to be uniform)
    delta = tau_u[lat_dim].values[1] - tau_u[lat_dim].values[0]


    # Calculate dx and dy using Earth's radius
    dx = delta * (np.pi / 180) * 6371e3
    dy = dx  # Assuming square grid
    
    # Central difference method for differentiation using xarray's roll method
    dtau_v_dx = (tau_v.roll({lon_dim: -1}, roll_coords=False) - tau_v.roll({lon_dim: 1}, roll_coords=False)) / (2 * dx)
    dtau_u_dy = (tau_u.roll({lat_dim: -1}, roll_coords=False) - tau_u.roll({lat_dim: 1}, roll_coords=False)) / (2 * dy)
    
    
    curl_tau = dtau_v_dx - dtau_u_dy  # N/m^3
    
    return curl_tau


def compute_ekman_transport(tau_u, tau_v, rho_water=1025):
    """
    Compute Ekman transport using 3D xarray DataArrays.
    
    Parameters:
    - tau_u, tau_v: Wind stress components in N/m^2 (3D xarray.DataArray, e.g., time, lat, lon).
    - rho_water: Seawater density in kg/m^3. Default is 1025 kg/m^3.
    
    Returns:
    - M_u, M_v: Ekman transport components in m^2/s (3D xarray.DataArray).
    - mean_Ekman: Absolute Ekman transport in m^2/s (3D xarray.DataArray).
    """
    
    ###### this part can be copied for the 2. Exercise ###########
    # Automatically detect the dimension name for latitude
    lat_dim = [dim for dim in tau_u.dims if 'lat' in dim or 'latitude' in dim][0]
    
    # Extract latitude values from the tau_u dataset
    lats = tau_u[lat_dim]


    omega = 7.2921e-5  # Earth's angular velocity (rad/s)
    
    # Calculate Coriolis parameter f using xarray's broadcasting
    f = 2. * omega * np.sin(np.deg2rad(lats))
    
    # Mask out poles and equator regions
    mask = (np.abs(lats) > 3) & (np.abs(lats) < 87)
    f = xr.where(mask, f, np.nan)
    
    
    # Broadcasting f (which is 1D, depending only on latitude) to match the 3D shape of tau_u (time, lat, lon).
    # This ensures that f is applied across all time and longitude dimensions consistently.
    f_3d = f.broadcast_like(tau_u)  #<- Tip for 2. Exercise replace tau_u
    ##################################################################

    # Calculate Ekman transport over all dimensions (including time)
    M_u = tau_v / (f_3d * rho_water)  # m^2/s
    M_v = -tau_u / (f_3d * rho_water)  # m^2/s
    mean_Ekman = np.sqrt(M_u**2 + M_v**2)
    
    return M_u, M_v, mean_Ekman


def compute_ekman_pumping(curl_tau, rho_water=1025):
    """
    Compute Ekman pumping velocity using 3D xarray DataArrays.
    
    Parameters:
    - curl_tau: Curl of wind stress in N/m^3 (3D xarray.DataArray, e.g., time, lat, lon).
    - rho_water: Water density in kg/m^3. Default is 1025 kg/m^3.
    
    Returns:
    - w_E: Ekman pumping velocity in m/s (3D xarray.DataArray).
    """

    
    # Automatically detect the dimension name for latitude
    lat_dim = [dim for dim in curl_tau.dims if 'lat' in dim or 'latitude' in dim][0]
    
    # Extract latitude values from the tau_u dataset
    lats = curl_tau[lat_dim]
    omega = 7.2921e-5  # Earth's angular velocity (rad/s)
    
    # Calculate Coriolis parameter f using xarray's broadcasting
    f = 2. * omega * np.sin(np.deg2rad(lats))
    
    # Mask out poles and equator regions
    mask = (np.abs(lats) > 3) & (np.abs(lats) < 87)
    f = xr.where(mask, f, np.nan)
    
    # Broadcasting f (which is 1D, depending only on latitude) to match the 3D shape of curl_tau (time, lat, lon).
    # This ensures that f is applied across all time and longitude dimensions consistently.
    f_3d = f.broadcast_like(curl_tau)
    
    # Compute Ekman pumping velocity over all dimensions (including time)
    w_E = curl_tau / (rho_water * f_3d)  # m/s
    
    return w_E




def compute_ekman_properties(u, v, rho_air=1.293, Cd=1.3e-3, rho_water=1025):
    """
    Compute Ekman transport and Ekman pumping from wind velocity components.
    
    Parameters:
    - u, v: Wind velocity components in m/s (3D xarray.DataArray: time, lat, lon).
    - Cd: Drag coefficient. Default is 1.3e-3.
    - rho_water: Water density in kg/m^3. Default is 1025 kg/m^3.
    
    Returns:
    - curl_tau: Wind stress curl in N/m^3 (3D xarray.DataArray: time, lat, lon).
    - M_u, M_v: Ekman transport components in m^2/s (3D xarray.DataArray: time, lat, lon).
    - mean_Ekman: Absolute Ekman transport in m^2/s (3D xarray.DataArray: time, lat, lon).
    - w_E: Ekman pumping velocity in m/s (3D xarray.DataArray: time, lat, lon).
    """
    
    # Compute wind stress
    tau_u, tau_v = compute_windstress(u, v, rho_air, Cd)
    
    # Compute curl of wind stress
    curl_tau = compute_windstress_curl(tau_u, tau_v,)
    
    # Compute Ekman transport
    M_u, M_v, mean_Ekman = compute_ekman_transport(tau_u, tau_v)

    
    # Compute Ekman pumping velocity
    w_E = compute_ekman_pumping(curl_tau, rho_water)

    
    return curl_tau, M_u, M_v, mean_Ekman, w_E

def compute_ekman_properties_from_stress(tau_u, tau_v, rho_water=1025):
    """
    Compute Ekman transport and Ekman pumping from wind velocity components.
    
    Parameters:
    - u, v: Wind velocity components in m/s (3D xarray.DataArray: time, lat, lon).
    - 
    
    Returns:
    - curl_tau: Wind stress curl in N/m^3 (3D xarray.DataArray: time, lat, lon).
    - M_u, M_v: Ekman transport components in m^2/s (3D xarray.DataArray: time, lat, lon).
    - mean_Ekman: Absolute Ekman transport in m^2/s (3D xarray.DataArray: time, lat, lon).
    - w_E: Ekman pumping velocity in m/s (3D xarray.DataArray: time, lat, lon).
    """
    
    
    # Compute curl of wind stress
    curl_tau = compute_windstress_curl(tau_u, tau_v)
    
    # Compute Ekman transport
    M_u, M_v, mean_Ekman = compute_ekman_transport(tau_u, tau_v)

    
    # Compute Ekman pumping velocity
    w_E = compute_ekman_pumping(curl_tau, rho_water)

    
    return curl_tau, M_u, M_v, mean_Ekman, w_E
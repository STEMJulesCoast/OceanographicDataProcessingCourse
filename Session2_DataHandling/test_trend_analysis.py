# test_trend_analysis.py

import numpy as np
import xarray as xr
import pytest
from trend_analysis import adjust_longitude

def test_adjust_longitude_with_central_lon_0():
    # Arrange
    lon = np.array([0, 90, 180, 270, 360])
    data = xr.Dataset({'lon': (['lon'], lon)})
    expected_lon_0 = np.array([0, 90, 180, -90, 0])
    expected_lon_0.sort()

    # Act
    adjusted_data_0 = adjust_longitude(data, central_lon=0)
    
    # Assert
    assert np.array_equal(adjusted_data_0['lon'].values, expected_lon_0)


def test_adjust_longitude_with_central_lon_180():
    # Arrange
    lon = np.array([-200, -150, -100, -50, 0, 50, 100, 150, 200])
    data = xr.Dataset({'lon': (['lon'], lon)})
    expected_lon_180 = np.array([160, 210, 260, 310, 0, 50, 100, 150, 200])
    expected_lon_180.sort()
    
    # Act
    adjusted_data_180 = adjust_longitude(data, central_lon=180)
    adjusted_lon_180 = adjusted_data_180['lon'].values
    adjusted_lon_180.sort()
    
    # Assert
    assert np.array_equal(adjusted_lon_180, expected_lon_180), f"Expected {expected_lon_180}, but got {adjusted_lon_180}"

def test_adjust_longitude_invalid_central_lon():
    # Arrange
    lon = np.array([0, 90, 180, 270, 360])
    data = xr.Dataset({'lon': (['lon'], lon)})
    with pytest.raises(ValueError):
        adjust_longitude(data, central_lon=100)

if __name__ == '__main__':
    pytest.main()
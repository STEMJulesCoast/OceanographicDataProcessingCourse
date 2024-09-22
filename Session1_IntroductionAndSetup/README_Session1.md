# Introduction to Oceanographic Data Processing: Setting Up the Environment and Analyzing Global Datasets

This notebook is part of an introductory session on oceanographic data processing. The primary goal is to set up a Python-based data analysis environment, install the necessary libraries, and begin working with climate data. We will focus on exploring the structure of scientific datasets and preparing for in-depth analysis.

----
### Overview:
-----
1. **Setting Up the Environment**: 
   - The session begins by creating a virtual environment and installing essential Python libraries (`numpy`, `xarray`, `matplotlib`, `geopandas`, etc.) required for scientific data analysis.
   - managing a Python environment and installing dependencies.

2. **Downloading and Loading Data**: 
   - Once the environment is set up, we analyze oceanographic data, such as global wind data, in NetCDF format from Copernicus Marine Service.
   - We also work with additional geographic data (shapefiles for continents and country borders) from Natural Earth for visualization purposes.

3. **Exploring Data Structures**: 
   - We will learn how to open, inspect, and explore the contents of large scientific datasets using the `xarray` library.
   - We will review how data is organized in dimensions, coordinates, and attributes, providing a foundation for understanding complex data.

4. **Basic Data Visualization**: 
   - We create visualizations to explore the spatial distribution of data variables.
   - Techniques such as plotting data on 2D maps and overlaying geographic features using libraries like `matplotlib` and `geopandas` are covered.

5. **Analyzing Data**: 
   - Beyond visualization, we will experiment with data slicing and manipulation to extract specific regions of interest.
   - We'll introduce basic statistical techniques such as calculating spatial means and standard deviations for different regions.

### Key Learning Outcomes:

- **Environment Setup**: Learn how to create and manage Python virtual environments and install necessary scientific libraries.
- **Data Exploration**: Understand how to explore large NetCDF datasets using `xarray`, inspecting their structure, metadata, and content.
- **Basic Visualization**: Gain skills in visualizing data with `matplotlib` and overlaying geographical data with `geopandas`.
- **Data Slicing/Downsampling and Analysis**: Learn how to manipulate large datasets, focusing on specific regions or variables, and perform basic statistical analysis.

### Requirements:
- Python 3.12
- Required libraries: `numpy`, `xarray`, `matplotlib`, `geopandas`, `basemap`, `emoji`
- Download Shapefiles Natural Earth: [110m Cultural Vectors](https://www.naturalearthdata.com/downloads/110m-cultural-vectors/)
- Download Wind Data (Copernicus Marine Service): [Wind Data](https://data.marine.copernicus.eu/product/WIND_GLO_PHY_CLIMATE_L4_MY_012_003/files?path=WIND_GLO_PHY_CLIMATE_L4_MY_012_003%2Fcmems_obs-wind_glo_phy_my_l4_P1M_202211%2F2023%2F)


# **Transitioning from Surface Data to Vertical Profiles**

This notebook is part of the fifth session on oceanographic data processing, where we transition from focusing on surface data to exploring vertical profiles using Argo data. In this session, we work with objectively gridded Argo datasets, which provide temperature, salinity, and their uncertainties at various depths. Unlike previous sessions where we accessed sea surface temperature (SST) data via OPeNDAP, we now download and process gridded Argo data over HTTPS. This incorporates robust data handling with logical conditions to ensure that downloads, file handling, and data processing occur correctly.

---

### **Overview**:
---

1. **Downloading and Processing Argo Data**:
   - We begin by downloading Argo datasets using a list of URLs from the [Met Office website](https://www.metoffice.gov.uk/hadobs/en4/download-en4-2-2.html). Logical conditions (`if-else` statements) are used to handle errors and ensure that files are downloaded, unzipped, and correctly processed.

2. **Exploring Vertical Profiles**:
   - We transition from surface data to vertical profiles by visualizing temperature and salinity at various depths.
   - We calculate potential density using temperature and salinity data, and analyze sections across different ocean basins, focusing on both horizontal and vertical patterns. We compare temperature and salinity distributions.


3. **Mixed Layer Depth (MLD) Analysis**:
   - Mixed Layer Depth is calculated using a density threshold approach. We explore how changes in temperature and salinity impact the density structure of the ocean, and how this affects the MLD.
   - We calculate and visualize the seasonal cycle amplitude of the MLD, Mixed Layer Salinity and Mixed Layer Temperature.

4. **RMSE Analysis**:
   - We calculate the Root Mean Square Error (RMSE) between salinity/temperature in the first depth layer and the mixed layer. This analysis helps assess whether surface measurements are good proxies for mixed layer conditions.

---

### **Files Included**:

- [`session_5_notebook.ipynb`](/Session5_VariabilityAnalysis/session_5_notebook.ipynb): The main notebook for the session, which contains exercises and analyses focused on vertical profiles, MLD, and RMSE calculations.
- [`IntroGridding.ipynb`](/Session5_VariabilityAnalysis/IntroGridding.ipynb): An introductory notebook that explores gridding techniques for in situ data. 

### **Files Created**
- `EN4_uppermost_2020_2023.nc`: A subset of the gridded Argo data, saved after processing, containing salinity, potential density, and MLD data at the uppermost depth layer and stored in [`Data/EN4`](/Data/EN4/).

---

### **Key Learning Outcomes**:

- **Transitioning to Vertical Profiles**: Learn to analyze oceanographic data at different depths and compare horizontal and vertical structures across ocean basins.
- **Potential Temperature and Density Calculations**: Use the Gibbs SeaWater (GSW) library to calculate potential temperature and potential density, helping to better understand the vertical structure of the ocean. Learn more about GSW at [TEOS-10 GSW](https://www.teos-10.org/pubs/gsw/html/gsw_contents.html).  
- **Mixed Layer Dynamics**: Calculate the Mixed Layer Depth (MLD) based on density thresholds and examine its seasonal and interannual variability.  
- **Data Processing and Error Handling**: Implement logical conditions using `if-else` statements to manage data downloads, file handling, and ensure that the processing pipeline runs smoothly and only when the necessary data is available.
- **RMSE Analysis**: Assess the accuracy of surface measurements as proxies for mixed layer conditions by calculating the RMSE for salinity between the surface layer and the mixed layer.
- **Data Visualization**: Develop skills in plotting and visualizing multidimensional oceanographic data using interactive tools like `hvplot` to explore patterns across time, latitude, longitude, and depth.
- **Gridding Techniques**: Learn the basics of gridding in situ data using the [`IntroGridding.ipynb`](/Session5_VariabilityAnalysis/IntroGridding.ipynb) notebook, which introduces linear interpolation and objective mapping techniques.

---

This session builds on previous work with surface data and extends the analysis by incorporating vertical profiles and mixed layer dynamics.

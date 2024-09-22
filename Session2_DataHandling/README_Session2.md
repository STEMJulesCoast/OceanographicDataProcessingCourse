
# **Exploring Oceanographic Data with Python**

This notebook is part of the second session on oceanographic data processing. In this session, we will focus on handling large climate datasets, implementing loops, and calculating variability at different timescales. We'll also delve into statistical analysis, including the calculation of means, standard deviations, trends, and SST composites related to El Niño and La Niña events.

---

### **Overview**:
---
1. **Data Handling and Slicing**:
   - The session begins with an introduction to loading, handling, and slicing multidimensional datasets using Python’s `xarray` library.
   - We explore wind and sea surface temperature (SST) data, focusing on specific regions like the Indian Ocean and specific time ranges (e.g., the year 2023 and a longer period from 1960-2023).

2. **Calculating Variability on Different Timescales**:
   - We calculate and visualize **mean** and **standard deviation** values for SST and wind speed, revealing the variability at different temporal and spatial scales.
   - Seasonal cycles and interannual fluctuations are analyzed.

3. **Looping Through Datasets**:
   - We introduce loops to iterate over monthly datasets, enabling the calculation of monthly averages for regions of interest.
   - We will apply loops to compute and plot time series data, providing insights into the temporal variability of oceanographic variables.

4. **Statistical Analysis**:
   - We dive deeper into time series analysis, computing **trends** across decades and examining the long-term changes in SST.
   - Anomalies are computed and detrended to remove long-term trends

5. **Composites and Climate Events (ENSO)**:
   - We compute **SST composites** based on El Niño and La Niña events, isolating and analyzing the SST anomalies during these climate events.
   - Using an external script, we streamline the analysis, making it easier to calculate ENSO-related SST composites and plot the results for better insights.

---
### Files Included:

- `session_2_notebook.ipynb`: The main notebook.
- `trend_analysis.py`: A module for calculating and plotting trends.
- `enso_functions.py`: A module for calculating and plotting ENSO-related composites.

## **Key Learning Outcomes**:

- **Data Handling**: techniques for loading, slicing, and analyzing multidimensional climate data using `xarray`.
- **Iterating Through Data**: Use loops to process large datasets and perform repetitive calculations.
- **Statistical Analysis**: Calculate and interpret statistical metrics like **means**, **standard deviations**, and **trends** on various timescales.
- **Trend Analysis**: Identify and visualize long-term climate trends in oceanographic data.
- **ENSO Composites**: Identify and analyze climate events like El Niño and La Niña through SST composites.
  
---


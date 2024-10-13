
# Oceanographic Data Processing Course

Welcome to **Oceanographic Data Processing**. This course is designed to introduce you to working with oceanographic datasets using Python. It is divided into six sessions, each focusing on a different aspect of data processing, analysis, and visualization.

The course is organized into three meetings, each containing two sessions. The meetings will take place on November 2, November 30, and January 11.

## Course Structure:

The course consists of six sessions, each contained in its own folder:
- **Session 1**: Introduction to Data Structures and Basic Visualization
- **Session 2**: Working with Climate Data
- **Session 3**: Functions, Modules and Introduction into Wind Driven Ocean Dynamics
- **Session 4**: Analysis of Wind-Driven Ocean Dynamics: Ekman Transport and Vertical Motion
- **Session 5**: Variability Analysis of 4D-Oceanographic Data 
- **Session 6**: Frequency Patterns and Object-Oriented Programming – Introducing Fourier Transforms, Wavelets, and EOF Analysis

### Folder Structure:
- **`/Modules`**: Folder to store modules and containing the class `TimeSeriesAnalyzer`
- **`/Data`**: Folder to store datasets for each session.
- **`/Homework`**: Contains tasks for you to solve between meetings.
- **`/Session1_IntroductionAndSetup`**: Contains the notebook and materials for Session 1.
- **`/Session2_DataHandling`**: Contains the notebook and materials for Session 2.
- **`/Session3_FunctionsModules`**: Contains the notebook and materials for Session 3.
- **`/Session4_EkmanAnalysis`**: Contains the notebook and materials for Session 4.
- **`/Session5_VariabilityAnalysis`**: Contains the notebook and materials for Session 5.
- **`/Session6_FreqPatternsOOP`**: Contains the notebook and materials for Session 6.


-   solution notebooks will be uploaded after the course.
  
Each session folder contains a Jupyter notebook with both teaching materials and exercises. Solutions to the exercises will be uploaded after the course.


**Note:** Each notebook contains a few exercises, which we will either discuss together or you will complete independently. There are also extra exercises, but you don't need to do them. They are provided to deepen your understanding, but they are not required to progress through the script during our live sessions. If you find that you're moving through the material quickly and would like an additional challenge, feel free to tackle these as well.

**Homework will be uploaded to the `Homework` folder after every second session and must be completed before the next meeting. The first homework is already available but should only be worked on after the first meeting.**

**The course emphasizes the importance of carefully reading and understanding instructions and comments to find solutions.** 


### Requirements:

Before starting the course, make sure to:
1. Install Python 3.12 and Visual Studio Code (with the Jupyter extension). You can also use Anaconda.
2. Download the GitHub repository, unzip the folder, and make yourself familiar with the structure. 
3. Download the required datasets:
    - Download Wind Data (Copernicus Marine Service): [Wind Data](https://data.marine.copernicus.eu/product/WIND_GLO_PHY_CLIMATE_L4_MY_012_003/files?path=WIND_GLO_PHY_CLIMATE_L4_MY_012_003%2Fcmems_obs-wind_glo_phy_my_l4_P1M_202211%2F2023%2F) (12 files, one for each month of 2023) and store them in
   `Data/Wind` directory.
4. Please note that we will be working with Jupyter Notebooks throughout the course, and during the first session, we will install the necessary libraries and set up the virtual environment together.

---
FYI How to create a virtual environment and install the necessary libaries in Visual Studio Code

1. **Create a virtual environment** (optional, but recommended):
    ```bash
    python -m venv .venv
    ```

2. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

3. **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

---

### Access the course via Binder

Click the link below to launch the course in a temporary, browser-based environment using Binder. Binder allows you to run the Jupyter notebooks without needing to install anything locally. Keep in mind that this environment is temporary and any changes you make will be lost once you close the session or after ~10 minutes of inactivity. For a permanent setup, you may prefer to clone the GitHub repository and work in your local environment.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/STEMJulesCoast/OceanographicDataProcessingCourse/main)

---
## Data Utilized Throughout the Course

**Wind**:   
E.U. Copernicus Marine Service Information; DOI: https://doi.org/10.48670/moi-00181

**SST**:   
NOAA Extended Reconstructed SST V5 data provided by the NOAA PSL, Boulder, Colorado, USA, from their [website](https://psl.noaa.gov)

**Argo**:   
EN.4.2.2 (analysis.g10) data were obtained from https://www.metoffice.gov.uk/hadobs/en4/ and are © British Crown Copyright, Met Office, provided under a Non-Commercial Government Licence http://www.nationalarchives.gov.uk/doc/non-commercial-government-licence/version/2/.

--- 
### License

This work is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). To view a copy of this license, visit [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/).

### Third-Party Libraries and Licenses

This project uses the following third-party libraries, which are licensed separately:

- **NumPy** (BSD 3-Clause License)
- **Matplotlib** (Matplotlib License - BSD-like)
- **Xarray** (Apache License 2.0)
- **Pandas** (BSD 3-Clause License)
- **GeoPandas** (BSD 3-Clause License)
- **Emoji** (BSD 3-Clause License)
- **netCDF4** (MIT License)
- **h5netcdf** (MIT License)
- **SciPy** (BSD 3-Clause License)
- **Basemap** (MIT License)
- **Dask** (BSD 3-Clause License)
- **nc-time-axis** (MIT License)
- **Bokeh** (BSD 3-Clause License)
- **GSW** (BSD 3-Clause License)
- **HoloViews** (BSD 3-Clause License)
- **PyCWT** (BSD 3-Clause License)
- **EOFs** (MIT License)
- **hvPlot** (BSD 3-Clause License)
- **IPykernel** (BSD 3-Clause License)
- **IPython** (BSD 3-Clause License)
- **Jupyter Client** (BSD 3-Clause License)
- **Pytest** (MIT License)

Please see the respective library documentation and license files for more details.
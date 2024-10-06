
# Oceanographic Data Processing Course

Welcome to **Oceanographic Data Processing**. This course is designed to introduce you to working with oceanographic datasets using Python. It is divided into six sessions, each focusing on a different aspect of data processing, analysis, and visualization.

## Course Structure:

The course consists of six sessions, each contained in its own folder:
- **Session 1**: Introduction to Data Structures and Basic Visualization
- **Session 2**: Working with Climate Data
- **Session 3**: Functions, Modules and Introduction into Wind Driven Ocean Dynamics
- **Session 4**: Analysis of Wind-Driven Ocean Dynamics: Ekman Transport and Vertical Motion
- **Session 5**: Variability Analysis of 4D-Oceanographic Data 
- **Session 6**: Frequency Patterns and Object-Oriented Programming – Introducing Fourier Transforms, Wavelets, and EOF Analysis

### Folder Structure:
- **`Modules`**: Folder to store modules and containing the class `TimeSeriesAnalyzer`
- **`/Data`**: Folder to store datasets for each session.
- **`/Session1_IntroductionAndSetup`**: Contains the notebook and materials for Session 1.
- **`/Session2_DataHandling`**: Contains the notebook and materials for Session 2.
- **`/Session3_FunctionsModules`**: Contains the notebook and materials for Session 3.
- **`/Session4_EkmanAnalysis`**: Contains the notebook and materials for Session 4.
- **`/Session5_VariabilityAnalysis`**: Contains the notebook and materials for Session 5.
- **`/Session6_FreqPatternsOOP`**: Contains the notebook and materials for Session 6.


-   solution notebooks will be uploaded after the course.
  
Each session folder contains a Jupyter notebook with both teaching materials and exercises. Solutions to the exercises will be uploaded after the course.

[Click here to view the folder structure](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNp9lV1vozgUhv8K8tWulJLwOW0uRurko620nUbtaFa7JLIc7CRowM7YZlqm6n-fQ3CoRVLITcCvj5_35Ri_olRQhsZoK8l-5_zzuOQOXKpcNw8ehdDNo_q6_it5SBnh4jCYpVOiyUKKlCmV8e3qb0vpXFx8dr4kw3tBy5yp4cp5H_zSDHpJ8i0rmGIyYwoTTvLqN5PuvlqtTrR-kphKzpZxJolm1KGlhGUdvWPORJRSMXtil2WSDGvcoSWZNANeMvw34_TMiJ8Mn56-nRkIkuHsa3hmIEyGnjcqcFrmupQkP0oYp0veybZe1CrgGRqIJS1YobBYq4tn0OBtLvB-V-GiwnmIF9499kd-MPJcntqO2woQ1n-Qh0PFM88FoRDVJoPoVj0w4NOq5Bv_3vlKDuHUSUkOLonOBO-tDEFZlQMTIFSefXVD14ff4dUrptytN3KPS13kmdKuftF9tScmZmuB0LwIWGBem3Y2Qjo5ABdEwRoDZy0kZVI5TKdubyJ1V4O3biNNoSmaIQ_fcS2hLdM6hGtOn5gu93ZXTJsZwKKaKdjDXGi2FuKHm-0rvl6dquH1Pc6up_czfFzHLWit65LMWhIf1719Cy5z2BE2waxRWgR-D4FRnxD4hqCjC5KEcSXwpuSHCFRn8xpZmCRaQsTNHlfZUdb1M2_9BHh-LNl-QN7V80ZteQp6PBn1iaeg48noak8vpNjnrLX1XrNLfNMSh3j2oyDQBI1DG_emkVq4YQ-uUZ_ghh80wW2LEOHvRGZkneWZrs6B3DYTLJCoB8SoT0CiTm5GB7kddsONzCiFJvw4tLuWOMZzyX4uiNZMcvXwsLBp7xqxRRv30Br1CW3coTU6oH0mv1jONKasEB_Wg9adPczbxj0jtj4djb1rIF5UegfAE0A9xTWyFtUQogEqmCxIRuE4fq2lSwRHW8GWaAx_KdsQ-Not0ZK_gZSUWjxVPEVjLUs2QFKU2x0ab0iu4K7cUzghpxmBT1lxlDCaaSHvm_P-cOwP0J7w_4VoJXCLxq_oBY2D4Mr14_jSi7zLKArjqwGq4KkLNyM_Di-DKIg-xXH8NkC_DwVG7lXkx174KYguvfDKi8K3PzaRgFc)


**Note:** Each notebook contains a few exercises, which we will either discuss together or you will complete independently. There are also extra exercises, but you don't need to do them. They are provided to deepen your understanding, but they are not required to progress through the script. If you find that you're moving through the material quickly and would like an additional challenge, feel free to tackle these as well.

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


### License

This work is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). To view a copy of this license, visit [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/).

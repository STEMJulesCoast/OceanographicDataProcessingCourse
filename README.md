
# Oceanographic Data Processing Course

Welcome to **Oceanographic Data Processing**. This course is designed to introduce you to working with oceanographic datasets using Python. It is divided into six sessions, each focusing on a different aspect of data processing, analysis, and visualization.

## Course Structure:

The course consists of six sessions, each contained in its own folder:
- **Session 1**: Introduction to Data Structures and Basic Visualization
- **Session 2**: Working with Climate Data
- **Session 3**: Functions, Modules and Introduction into Wind Driven Ocean Dynamics
- **Session 4**: Analysis of Wind-Driven Ocean Dynamics: Ekman Transport and Vertical Motion
- **Session 5**: Statistical Analysis of Oceanographic Data
- **Session 6**: Final Session - Integrating Everything and Introducing Fourier Transformation

### Folder Structure:

- **`/Data`**: Folder to store datasets for each session.
- **`/Session1_IntroductionAndSetup`**: Contains the notebook and materials for Session 1.
- **`/Session2_DataHandling`**: Contains the notebook and materials for Session 2.
- **`/Session3_FunctionsModules`**: Contains the notebook and materials for Session 3.
- **`/Session4_EkmanAnalysis`**: Contains the notebook and materials for Session 4.
- **`/Session5_StatisticsAndTrends`**: Contains the notebook and materials for Session 5.
- **`/Session6`**: Contains the notebook and materials for Session 6.

-   solution notebooks will be uploaded after the course.
  
Each session folder contains a Jupyter notebook with both teaching materials and exercises. Solutions to the exercises will be uploaded after each session.

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

Click the link below to launch the course in a temporary, browser-based environment using Binder. Binder allows you to run the Jupyter notebooks without needing to install anything locally. Keep in mind that this environment is temporary and any changes you make will be lost once you close the session. For a permanent setup, you may prefer to clone the GitHub repository and work in your local environment.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/STEMJulesCoast/OceanographicDataProcessingCourse/main)


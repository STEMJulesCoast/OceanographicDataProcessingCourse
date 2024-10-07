# **Analysis of Wind-Driven Ocean Dynamics: Ekman Transport and Vertical Motion**

This notebook is part of the fourth session on oceanographic data processing. In this session, we focus on analyzing wind-driven ocean dynamics, specifically Ekman transport and vertical motion. We compare different methods of calculating Ekman properties using both annual mean and monthly wind data, demonstrating the effects of temporal resolution on variability and accuracy.

---

### **Overview**:
---
1. **Loading Wind Data**:
   - We begin by loading wind data for the year 2023 again, using monthly wind components from **reanalysis data** provided by CMEMS. 
   - The wind data will serve as the basis for our Ekman dynamics calculations.

2. **Ekman Dynamics Calculations**:
   - **Annual Mean Approach**: First, we calculate the Ekman transport, wind stress curl, and vertical Ekman velocity (`w_E`) based on the annual mean of wind data.
   - **Monthly Data Approach**: Then, we calculate the same Ekman properties for each month and take the average across all months.
   - We aim to understand the differences in results produced by these two methods.

3. **Introducing Decision Logic**:
   - One part of this session is integrating conditional decision-making using Python's `if-else` statements. Before performing the calculations, we check whether the wind data is correctly (down)loaded, allowing the code to only run when the necessary data is available.

4. **Comparing Results**:
   - After performing the calculations using both the annual mean and monthly data, we compare the results, particularly focusing on the variability in vertical Ekman velocity (`w_E`).
   - The comparison helps to highlight how different temporal resolutions influence the representation of variability in the results.

---

### Files Included:

- `session_4_notebook.ipynb`: The main notebook for the session, which contains the exercises and Ekman dynamics analysis.
- `ekman_dynamics.py`: A module created in Session 3, containing functions for calculating Ekman transport, wind stress curl, and vertical Ekman velocity. The module was generated in Session 3 and should be stored in the `Modules` folder.

---

### **Key Learning Outcomes**:

- **Ekman Dynamics**: We will gain a deeper understanding of wind-driven ocean dynamics, including the computation of wind stress, horizontal Ekman transport, and vertical Ekman velocity.
- **Temporal Resolution**: Explore how temporal resolution (annual mean vs. monthly data) affects the representation of climate processes and variability in the results.
- **Decision-Making in Code**: Learn how to implement `if-else` logic in Python to manage data loading and execution flow, ensuring calculations are only performed when the necessary conditions are met.
- **Data Visualization**: Develop skills in plotting and visualizing oceanographic data using Basemap and Matplotlib, producing meaningful maps to interpret wind-driven processes.

---

This session builds on the work from **Session 3**, where we developed the `ekman_dynamics.py` module. We now reuse this module to perform analyses and comparisons of wind-driven ocean dynamics.

---

## Done with the exercise of Session 3 and Session 4? 

Test your knowledge with this little [Quiz](https://stemjulescoast.github.io/QuizCollection/HCUquiz_ODP2.html)
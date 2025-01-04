# **Automating Frequency and Pattern Analysis: FFT, Wavelets, and OOP**

This notebook is part of the sixth session on oceanographic data processing. In this session, we focus on automating the analysis of frequency patterns within oceanographic datasets using Fast Fourier Transform (FFT) and Wavelet Analysis. By integrating these analyses into an object-oriented programming (OOP) framework, we streamline the processing of data for different variables, such as SST and wind, making the code more modular and reusable.

---

### **Overview**:
---
1. **Signal Processing**:
   - We begin with an introduction to signal analysis, focusing on identifying dominant frequencies in SST anomalies. This is essential for detecting oceanic phenomena such as ENSO and other climatic cycles.
   - Using FFT, we identify the dominant periods in the SST data, highlighting the key frequencies that contribute to variability.

2. **Wavelet Analysis**:
   - Wavelet analysis is then introduced to provide a time-localized view of the dominant frequencies. This method allows us to track how these frequencies evolve over time, offering more insight than the global perspective provided by FFT.

3. **Object-Oriented Programming (OOP)**:
   - With OOP, we streamline repetitive tasks by organizing our code into a class structure, which allows us to apply the same analyses across different datasets.


4. **Application to Wind Data**:
   - After analyzing SST, you apply the same methods to wind data, including the calculation of Ekman properties. The [`TimeSeriesAnalyzer`](/Modules/timeseries_analyzer.py) class is reused to automate the analysis for wind-driven processes.

5. **EOF Analysis (Extra)**:
   - As an additional step, we introduce Empirical Orthogonal Function (EOF) analysis, which is used to identify dominant modes of variability in spatiotemporal data. An additional notebook ([`EOF_analysis_demo.ipynb`](/Session6_FreqPatternsOOP/EOFanalysis_demo.ipynb)) is provided for a detailed example of this technique.

---

For a general overview of how object-oriented modeling and programming work, please visit this [Storymap](https://storymaps.arcgis.com/stories/dd9d06f89a63400c96927de117a5b28a). The text is in German, but most browsers offer automatic translation. The article provides a closer look at the programming paradigm and dives into the benefits of encapsulation, inheritance, polymorphism, and abstraction.

---


### Files Included:

- [`session_6_notebook.ipynb`](/Session6_FreqPatternsOOP/session_6_notebook.ipynb): The main notebook for this session, which contains the exercises and automation of frequency analysis using FFT, wavelet analysis, and OOP.
- [`timeseries_analyzer.py`](/Modules/timeseries_analyzer.py): A Python module that contains the class. This class automates the computation of climatology, anomalies, detrending, FFT, and wavelet analyses and is stored in the [`Modules`](/Modules/) Folder.
- [`wavelet_demo.ipynb`](/Session6_FreqPatternsOOP/wavelet_demo.ipynb): Demonstrates the wavelet analysis process visually.
- [`EOFanalysis_demo.ipynb`](/Session6_FreqPatternsOOP/EOFanalysis_demo.ipynb): Demonstrates how to perform EOF analysis on the same datasets used in the session.
- additionaly the module [`ekman_dynamics.py`](../Modules/ekman_dynamics.py) created in Session 4 should be stored in the [`Modules`](/Modules/) Folder.
---

### **Key Learning Outcomes**:

- **Frequency Analysis**: Gain an understanding of how FFT and wavelet analysis can be used to detect dominant cycles and understand variability in oceanographic data.
- **Wavelet Power Spectrum**: Learn how to examine the evolution of significant periods over time, identifying key climate cycles such as ENSO and their temporal variations.
- **Object-Oriented Programming (OOP)**: Develop skills in OOP by automating data analysis with the [`TimeSeriesAnalyzer`](/Modules/timeseries_analyzer.py) class, allowing for reuse of code across multiple datasets.
- **Comparison of Variables**: Apply the same analytical techniques to both SST and wind data, and compare the variability in these datasets, particularly focusing on the role of Ekman dynamics in influencing SST patterns.
- **EOF Analysis (Extra)**: Extend the analysis to explore spatial patterns of variability using EOF analysis, providing a deeper understanding of the underlying dynamics driving changes in oceanographic data.

---

This session builds on previous work. Now, by integrating frequency analysis techniques, we deepen our exploration of the variability present in climate data over time and space.

---

## Done with the exercises of Session 5 and Session 6?

Challenge your understanding with this [Quiz](https://stemjulescoast.github.io/QuizCollection/HCUquiz_ODP3.html).



# **Understanding Functions and Modules in Python**

This notebook is part of the third session on oceanographic data processing. In this session, we will focus on creating and utilizing Python functions and modules. We begin with a simple exercise on functions, demonstrating their key benefits such as modularity, reusability, and readability. Then, we gradually introduce **Ekman dynamics** and explore how to organize related functions into a module for future use in subsequent sessions.

---

### **Overview**:
---
1. **Introduction to Functions**:
   - We start with the basics of defining and using functions in Python, emphasizing the importance of modularity, error reduction, and parameterization.
   - A hands-on example calculates the area of rectangles and squares using a function. This example will help solidify the understanding of basic function structure.

2. **Exercise: Circle Area Calculation**:
   - You will create a function to calculate the area of a circle. This allows for practice with function definitions and parameterization.

3. **Creating a Python Module**:
   - We organize functions into a Python module. This step involves creating a `.py` script with all necessary functions and importing it into the main notebook.
   - We walk through the process of saving and importing the module for use in later sessions.

4. **Ekman Dynamics**:
   - After reviewing the basics of functions, we transition into **Ekman dynamics**—an important concept in physical oceanography.
   - We create custom functions to calculate wind stress and curl, Ekman transport, and Ekman pumping. These functions are then organized into a Python module (`ekman_dynamics.py`) for use in **Session 4**.

---

### Files Included:

- `session_3_notebook.ipynb`: The main notebook.
- `example_function.ipynb`: A notebook for experimenting with simple functions.

### Files Created:
- `geometry.py`: A module for basic geometry functions like calculating areas.
- `ekman_dynamics.py`: A module for calculating Ekman properties.

---

## **Key Learning Outcomes**:

- **Functions**: Understanding how to create reusable and modular functions for different tasks in Python.
- **Modules**: Learn how to organize related functions into Python modules to improve code structure and reusability across projects.
- **Ekman Dynamics**: Introduction to wind-driven ocean dynamics, including the computation of wind stress, Ekman transport, and vertical Ekman velocity.
- **Debugging**: Learn how to debug by checking variable contents, shapes, and dimensions, using assertions to validate data, and plotting results to compare with literature.
- **Preparation for Session 4**: Create a custom module (`ekman_dynamics.py`) that will be reused in Session 4 for analyzing wind data and Ekman dynamics.

---


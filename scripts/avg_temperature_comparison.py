#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 12:01:21 2023

@author: helenah
"""

# Importing the neccessary libraries
# The numpy library is used to perform mathematical operations
# Matplotlib is used for visualization purposes
import numpy as np
import matplotlib.pyplot as plt

# Data on x-axis, months
x1 = ["Jan", "Mar", "May", "Jul", "Sep", "Nov"]
x2 = ["Jan", "Mar", "May", "Jul", "Sep", "Nov"]
x3 = ["Jan", "Mar", "May", "Jul", "Sep", "Nov"]


# Data on y-axis
# Los Angeles, CA Average Monthly Low Temperature
y1 = [10, 12, 14, 19, 19, 12]

# Oklahoma Montly Low Temperature
y2 = [-3, 5, 15, 22, 18, 3]

# Wyoming Monthly Low Temperature
y3 = [-14, -8, 0, 5, 0, -9]


# This creates the figure that contains the data
fig, ax = plt.subplots(figsize=(10,7))

# This creates the individual lines with the data provided in the x and y sections
# Data is also given a specific marker, color and label to differentiate them
ax.plot(x1,y1, color="red", marker="o", label="Los Angeles, CA - Highest number of homeless")

ax.plot(x2,y2, color="blue", marker="o", label="Oklahoma City, OK - Middle")

ax.plot(x3,y3, color="green", marker="o", label="Jackson, WY - Lowest")

# This creates a legend, describing what location the lines correspond to
# It also adjusts the location of the legend in the graph
plt.legend(loc="upper right")

# This sets the boundaries of the y-axis values, lowest and highest, to properly capture the temperature intervals
plt.ylim(-20, 30)

# This creates a visual grid, making it easier to interpret the data
plt.grid(True)

# This sets the overall title of the graph, as well as titles of the axes
ax.set_title("Average Temperature in Three US States With Differing Homelessness Rates")
ax.set_xlabel("Month")
ax.set_ylabel("Temperature in Celsius")



plt.show()
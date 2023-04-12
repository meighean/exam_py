#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 11:59:12 2023

@author: helenah
"""

# Importing the neccessary libraries
# The numpy library is used to perform mathematical operations
# Matplotlib is used for visualization purposes
# Pandas are used for the purpioses of data analysis and manipulation
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Here I import the csv file containing the data I manipulate and visualize
df = pd.read_csv("/Users/helenah/Desktop/homelessness(1).csv")

# This prints the data so that it is displayed in the console of Spyder
print(df)

# This creates a smaller dataset so that I can adjust the number of items displayed.
# In this case, all of the 53 rows are displayed, but I can easily change it by adjusting the number.
df_small = df.iloc[0:53]


# This organizes the states into a list, making it easier to work with when combining with another list
states = list(df_small["state"])
# This organizes the individual column into a list and re-names it "people"
people = (df_small["individuals"])

# This sorts and combines the data in the two lists: individuals and state, and arranges it in descending order
people_sorted = sorted(people)
states_sorted = [st for _, st in sorted(zip(people, states))]

# This creates the figure
f, ax = plt.subplots(figsize=(4, 8))

# This creates a visible grid, making it easier to interpret
plt.grid(True)

# This creates the horizontal bar graph, with number of homeless individuals on the x-axis (as width), and states on the x-axis (height)
ax.barh(y=states_sorted, width=people_sorted, height=0.7, color="darkblue", edgecolor="orange")

# This creates the title and the name of the item of each axis
plt.title("Number of Homeless Individuals by US State")
plt.xlabel("Number of individuals")
plt.ylabel("State")


plt.show()
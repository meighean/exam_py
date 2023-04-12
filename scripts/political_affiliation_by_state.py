#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:25:21 2023

@author: helenah
"""

# The matplotlib library allows me to visualize data.
# The pandas library allows me to manipulate and analyze data.
import matplotlib.pyplot as plt
import pandas as np

# First pie chart depicts number of registered voters in California in 2022
# Labels denote the different parties
labels1 = ['Republicans', 'Democrats', 'Other']
# Sizes denote the different perecentages
sizes1 = [23.85, 46.87, 28.12]
# Colors denote the different colors corresponding to each party
colors1 = ['#f71a0f', '#0f3df7', '#abb2b9']

# Second pie chart depicts registered voters in Oklahoma in 2023
labels2 = ['Republicans', 'Democrats', 'Other']
sizes2 = [51.88, 29.48, 18.64]
colors2 = ['#f71a0f','#0f3df7','#abb2b9']

# Second pie chart depicts registered voters in Wyoming in 2023
labels3 = ['Republicans', 'Democrats', 'Other']
sizes3 = [82.09, 10.53, 7.38]
colors3 = ['#f71a0f', '#0f3df7', '#abb2b9']

# This command creates two figures (three subplots). 
# The numbers in the parentheses determine the arrangement: 1 row, 3 columns.
# I chose to have 1 row and 3 columns because of the ease of comparison.
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

# These commands utilize the data provided in the first two sections of the code, in addition to the autopct command that
# specifies that one decimal place and a percent sign should be displayed.
# Commands also adjusts the starting angle for the first wedge in the pie chart, meaning that it displays the first label at the top and continues counterclockwise.
ax1.pie(sizes1, labels=labels1, colors=colors1, autopct='%1.1f%%', startangle=90, textprops={'fontsize':7})
ax1.set_title('California', fontstyle="italic")

ax2.pie(sizes2, labels=labels2, colors=colors2, autopct='%1.1f%%', startangle=90, textprops={'fontsize':7})
ax2.set_title('Oklahoma', fontstyle="italic")

ax3.pie(sizes3, labels=labels3, colors=colors3, autopct='%1.1f%%', startangle=90, textprops={'fontsize':7})
ax3.set_title('Wyoming', fontstyle="italic")

# This adjusts the overarching title of the entire graph, in terms of font size and boldness
plt.suptitle('Presidental Election Votes by State', fontsize=18, fontweight="bold")

# This adjusts the horizontal (left and right commands) and vertical spacing (bottom and top). 
# Wspace ajusts the distance between the subplots.
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=1.1, wspace=0.6)


#%%
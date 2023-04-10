#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:12:50 2023

@author: helenah
"""

import matplotlib.pyplot as plt
import pandas as np

labels = ['Republicans', 'Democrats', 'Other']
sizes = [65.37, 32.29, 2.34]
colors = ['#f71a0f','#0f3df7','#abb2b9']


fig, (ax) = plt.subplots()

ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, textprops={'fontsize':7})
ax.set_title('Presidential Election Results for Oklahoma', fontstyle="italic")




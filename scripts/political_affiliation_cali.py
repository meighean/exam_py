#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:59:24 2023

@author: helenah
"""

import matplotlib.pyplot as plt
import pandas as np


labels1 = ['Republicans', 'Democrats', 'Other']
sizes1 = [23.85, 46.87, 28.12]
colors1 = ['#f71a0f', '#0f3df7', '#abb2b9']

fig, (ax1) = plt.subplots()

ax1.pie(sizes1, labels=labels1, colors=colors1, autopct='%1.1f%%', startangle=90, textprops={'fontsize':6.5})
ax1.set_title('Presidential Election Results for California', fontstyle="italic")


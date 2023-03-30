#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:12:13 2023

@author: helenah
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("/Users/helenah/Desktop/homelessness(1).csv")

print(df)

df_small = df.iloc[0:53]

states = list(df_small["state"])
people = (df_small["individuals"])

people_sorted = sorted(people)
states_sorted = [st for _, st in sorted(zip(people, states))]


f, ax = plt.subplots(figsize=(4, 8))

ax.barh(y=states_sorted, width=people_sorted, height=0.7, color="darkblue")


plt.title("Number of Homeless Individuals by US State")
plt.xlabel("Number of individuals")
plt.ylabel("State")


plt.show()
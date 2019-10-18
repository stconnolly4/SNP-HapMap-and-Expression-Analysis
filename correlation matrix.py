#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:45:44 2019

@author: Sami
"""
from matplotlib import pyplot as plt
import pandas
import seaborn as sns
import numpy as np


climate_data = pandas.read_csv("climate data for correlation matrix.csv", encoding = "ISO-8859-1", dtype = float)
filtered_climate_data = pandas.read_csv("filtered climate data for correlation matrix.csv", encoding = "ISO-8859-1", dtype = float)
#soil_data = pandas.read_csv("Medicago truncatula Soil Variables.csv", encoding = "ISO-8859-1", dtype = float)


corr = climate_data.corr()
filtered_corr = filtered_climate_data.corr()
#soil_corr = soil_data.corr()


corr.to_csv('climate data correlation.csv')
filtered_corr.to_csv('filtered climate data correlation.csv')
#soil_corr.to_csv('filtered soil data correlation.csv')

plt.figure(figsize=(10, 10))
figure = sns.heatmap(corr)
figure.set_title("Pearson's Correlation between Climate Variables")
plt.savefig("Pearson's Correlation between Climate Variables")

plt.figure(figsize=(10, 10))
plt.rcParams.update({'font.size': 12})
#figure = sns.heatmap(soil_corr)
figure.set_title("Pearson's Correlation between Filtered Climate Variables")
plt.savefig("Pearson's Correlation between Filtered Climate Variables")
#figure.set_title("Pearson's Correlation between Filtered Soil Variables")
#plt.savefig("Pearson's Correlation between Filtered Soil Variables")

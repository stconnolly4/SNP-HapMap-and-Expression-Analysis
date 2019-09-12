#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 10:49:58 2019

@author: Sami
"""

import statsmodels.stats.multitest as mt
import pandas

#this is the file I get from running weighted MLM in TASSEL"
filename = "MtGIRAFFE stats.csv"
dataframe = pandas.read_csv(filename, encoding = "ISO-8859-1", dtype = str)
#dataframe.sort_values(by=['p'])

p_vals = [float(i) for i in dataframe.p]

true_or_false, adjusted_p_vals = mt.fdrcorrection(p_vals, alpha=.05)

adjusted_signficant_results = []

for i in range(len(true_or_false)):
    if (true_or_false[i] == True):
        adjusted_signficant_results.append((dataframe.iloc[i,0], dataframe.iloc[i,3]))

with open('adjusted_signifance.txt', 'w') as outfile:
    for result in adjusted_signficant_results:
        outfile.write(result[0])
        outfile.write(" : ")
        outfile.write(result[1])
        outfile.write("\n")

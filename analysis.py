#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:15:57 2019

@author: Sami
"""

from accession import ACCESSION
import constants as c
import pandas
from SNP import SNP
import seaborn as sns
import matplotlib.pyplot as plt

# read in SNP data
SNP_data = pandas.read_csv(c.SNP_data_filename, encoding = "ISO-8859-1", dtype = str)
SNP_data_columns = list(SNP_data.columns)

# read in climate data
climate_data = pandas.read_csv(c.climate_data_filename, encoding = "ISO-8859-1", dtype = str)

# create a list of accessions with HM number and SNP data
accessions = []
count = 2
for index, row in SNP_data.iterrows():
    if (count < len(SNP_data_columns)):
        accessions.append(ACCESSION(SNP_data_columns[count]))
        accessions[count-2].add_SNPs(SNP_data.iloc[:,count])
        count += 1
 
# create a list of accession names that I have
HM_numbers_that_we_have = []
for accession in accessions:
    HM_numbers_that_we_have.append(accession.HM_number)          
       
 # add climate data to the list of accessions  
climate_counter = 0 
accessions_counter = 0 
for i in range(c.looping_constant):
    if (climate_data.iloc[climate_counter, 0] == accessions[accessions_counter].HM_number):
        accessions[accessions_counter].add_climate_data(climate_data.iloc[climate_counter])
        climate_counter += 1
        accessions_counter += 1
    # if the HM### is missing in the accessions
    elif climate_data.iloc[climate_counter, 0] not in HM_numbers_that_we_have:
        climate_counter += 1
    # if there is a duplicate
    elif (climate_data.iloc[climate_counter, 0] == climate_data.iloc[climate_counter-1, 0]):
        climate_counter += 1
    else:
        accessions_counter += 1
    
# add the accessions to the SNPs
SNPs_ratios = []
pos_index = 0
for pos in SNP_data.iloc[:,1]:
    temp_SNP = SNP(pos)
    for acc in accessions:
        temp_SNP.update_list(acc, pos_index)
    pos_index += 1
    SNPs_ratios.append(temp_SNP)

counts_for_nonbios_graphs = [0]*12
counts_for_bios_graphs = [0]*19

for s in SNPs_ratios:
    s.initialize_climate_data_updating()
    s.update_non_bios_climate_data()
    counts_for_nonbios = s.do_non_bios_stats(counts_for_nonbios_graphs)
    s.update_bios_climate_data()
    counts_for_bios = s.do_bioXX_stats(counts_for_bios_graphs)

f = open("Figures/counts.txt","w+")
f.write(c.geneID)
f.write("\n\n")
for i in range(len(c.labels_for_non_bios_graphs)):
    f.write(c.labels_for_non_bios_graphs[i] + ": " + str(counts_for_nonbios_graphs[i]))
    f.write("\n")
for i in range(len(c.labels_for_bios_graphs)):
    f.write(c.labels_for_bios_graphs[i] + ": " + str(counts_for_bios_graphs[i]))
    f.write("\n")
f.close()
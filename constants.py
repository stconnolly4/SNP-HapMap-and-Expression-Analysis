#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:14:05 2019

@author: Sami
"""

#SNP_data_filename = "MtNPF1B SNP data.csv"
#looping_constant = 184
#geneID = "MtNPF1B"

#SNP_data_filename = "MtNPF1B 5 prime 2kb SNP data.csv"
#looping_constant = 117
#geneID = "MtNPF1B 5 prime 2kb"

#SNP_data_filename = "MtNPF1B 3 prime 2kb SNP data.csv"
#looping_constant = 76
#geneID = "MtNPF1B 3 prime 2kb"

#SNP_data_filename = "MtLATD SNP data.csv"
#looping_constant = 97
#geneID = "MtLATD"

#SNP_data_filename = "MtLATD 5 prime 2kb SNP data.csv"
#looping_constant = 113
#geneID = "MtLATD 5 prime 2kb"

#SNP_data_filename = "MtLATD 3 prime 2kb SNP data.csv"
#looping_constant = 87
#geneID = "MtLATD 3 prime 2kb"

#SNP_data_filename = "MtNPF1D2 (057460) SNP data.csv"
#looping_constant = 292
#geneID = "MtNPF1D2 (057460)"

#SNP_data_filename = "MtNPF1D2 (101560) SNP data.csv"
#looping_constant = 292
#geneID = "MtNPF1D2 (101560)"

#SNP_data_filename = "MtNPF1D2 (101590) SNP data.csv"
#looping_constant = 292
#geneID = "MtNPF1D2 (101590)"

#SNP_data_filename = "MtNPF1D2 (2g101610) SNP data.csv"
#looping_constant = 208
#geneID = "MtNPF1D2 (2g101610)"

#SNP_data_filename = "MtNPF1D2 (2g101640) SNP data.csv"
#looping_constant = 97
#geneID = "MtNPF1D2 (2g101640)"

#SNP_data_filename = "MtNPF1D2 (2g101650) SNP data.csv"
#looping_constant = 84
#geneID = "MtNPF1D2 (2g101650)"

SNP_data_filename = "MtNPF1D2 (4g011280) SNP data.csv"
looping_constant = 217
geneID = "MtNPF1D2 (4g011280)"

#SNP_data_filename = "MtRBOHC SNP data.csv"
#looping_constant = 212
#geneID = "MtRBOHC"

#SNP_data_filename = "MtGIRAFFE SNP data.csv"
#looping_constant = 109
#geneID = "MtGIRAFFE"

p_value_cutoff = .05
percentage_cutoff = .1 #Minimum Allele Frequency

climate_data_filename = "Medicago_fset_climatic-country.csv" #exported .xlxs file as a CSV, deleted empty row below header, sorted by HapMap ID

climate_data_columns = ["HM_NUMBER", "ELEVACE", "LAT", "LON", "Country", "prec_1", 
                        "prec_2", "prec_3", "prec_4", "prec_5", "prec_6", "prec_7", 
                        "prec_8", "prec_9", "prec_10", "prec_11", "prec_12", "tmean_1",
                        "tmean_2", "tmean_3", "tmean_4", "tmean_5", "tmean_6", 
                        "tmean_7", "tmean_8", "tmean_9", "tmean_10", "tmean_11",
                        "tmean_12", "tmin_1", "tmin_2", "tmin_3", "tmin_4", 
                        "tmin_5", "tmin_6", "tmin_7", "tmin_8", "tmin_9", "tmin_10", 
                        "tmin_11", "tmin_12", "tmax_1", "tmax_2", "tmax_3", "tmax_4",
                        "tmax_5", "tmax_6	", "tmax_7", "tmax_8", "tmax_9", "tmax_10",
                        "tmax_11", "tmax_12",	"bio_1", "bio_2", "bio_3", "bio_4", 
                        "bio_5", "bio_6", "bio_7", "bio_8", "bio_9", "bio_10", "bio_11", 
                        "bio_12", "bio_13", "bio_14", "bio_15", "bio_16", "bio_17", 
                        "bio_18", "bio_19", "AWCtS", "AWCh1", "WWP", "BLDFIE", "CECSOL", 
                        "CLYPPT", "SLTPPT", "SNDPPT", "CRFVOL"	, "ORCDRC", "pH1", "pH2"]

labels_for_bios_graphs = ["Annual Mean Temperature", 
                          "Annual Mean Diurnal Range", 
                          "Isothermality", 
                          "Temperature Seasonality (Standard Deviation)",
                          "Max Temperature of the Warmest Month",
                          "Min Temperature of the Coldest Month", 
                          "Annual Temperature Range",
                          "Mean Temperature of Wettest Quarter",
                          "Mean Temperature of Dryest Quarter",
                          "Mean Temperature of Warmest Quarter", 
                          "Mean Temperature of Coldest Quarter",
                          "Annual Precipitation", 
                          "Precipitation of Wettest Month", 
                          "Precipitation of Driest Month", 
                          "Precipitation Seasonality (CV)", 
                          "Precipitation of Wettest Quarter", 
                          "Precipitation of Driest Quarter", 
                          "Precipitation of Warmest Quarter", 
                          "Precipitation of Coldest Quarter"]

y_axis_labels_for_bios_graphs = ["Degrees Celsius (x10)", 
                                 "Degrees Celsius (x10)", 
                                 "Percent", 
                                 "Degrees Celsius (x10)",
                                 "Degrees Celsius (x10)",
                                 "Degrees Celsius (x10)", 
                                 "Degrees Celsius (x10)",
                                 "Degrees Celsius (x10)",
                                 "Degrees Celsius (x10)",
                                 "Degrees Celsius (x10)", 
                                 "Degrees Celsius (x10)",
                                 "Millimeters", 
                                 "Millimeters", 
                                 "Millimeters", 
                                 "Percent", 
                                 "Millimeters", 
                                 "Millimeters", 
                                 "Millimeters", 
                                 "Millimeters"]

labels_for_non_bios_graphs = ["Saturated Water Content", 
                              "Available Soil Water Capacity", 
                              "Available Soil Water Capacity until wilting point", 
                              "Bulk Density", 
                              "Cation Exchange Capacity of Soil", 
                              "Clay Content", 
                              "Silt Content", 
                              "Sand Content", 
                              "Coarse Fragments",
                              "Soil Organic Carbon Content",
                              "Soil pH in H2O",
                              "Soil pH in KCl"]

y_axis_labels_for_non_bios_graphs = ["Volumetric Fraction", 
                                      "Volumetric Fraction", 
                                      "Volumetric Fraction", 
                                      "???", 
                                      "???", 
                                      "Mass Fraction", 
                                      "Mass Fraction", 
                                      "Mass Fraction", 
                                      "Percent",
                                      "g/kg",
                                      "pH",
                                      "pH"]
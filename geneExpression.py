import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import kruskal
import os
import numpy as np

species = "Medicago truncatula"
termsToSearchBy = ["root", "nodule", "shoot", "leaf", "stem", "seed", "myc"]
#termsToSearchBy = []
filepath = species + "/"
fileFormat = "txt"

def get_expression(species_gene, condition_or_part, all_data):
    keys = all_data[species_gene][0] # the keys are the conditions/parts. example: 'mean_nod21_1'
    values = all_data[species_gene][1] # the values are the corresponding numeric expression levels. example: 18.66
    
    # indices will be filled with integers representing the indices in keys, and can be used to determine corresponding expression levels from values.
    indices = []
    # after indices are determined, we loop through and find coresponding values. these values will be added to expression_levels and then returned.
    expression_levels = []
    
    for i in range(len(keys)):
        # if we are checking "root", then add (1) "root" only, (2) "root" & "non-myc", 
        # but NOT (3) "root" & "myc" and NOT (4) "root" & "nodule"
        if condition_or_part == "root":
            if "root" in keys[i]: # options (1), (2), (3), and (4)
                if "myc" in keys[i]: # options (2) and (3)
                    if "non-myc" in keys[i]: # option (2). option (3) has been eliminated.
                        indices.append(i) # ADD OPTION (2)
                elif "nodule" not in keys[i]: # eliminate option (4), only option (1) remains
                    indices.append(i) # ADD OPTION (1)
        
        # if we are checking "myc", then add (1) "myc", but NOT (2) "non-myc"
        elif condition_or_part == "myc":
            if "myc" in keys[i]: # options (1) and (2)
                if "non-myc" not in keys[i]: # option (1). option (2) has been eliminated
                    indices.append(i) # ADD OPTION (1)
        
        # all other parts of plant            
        elif condition_or_part in keys[i]:
            indices.append(i)
                
    for index in indices:
        expression_levels.append(values[index])
    
    return expression_levels

all_data = {}
keys_list = []


            
if (species == "Medicago truncatula" and fileFormat == "txt"):
    for filename in os.listdir(filepath):
        try:
            infile = open(filepath + filename)
            raw = infile.readlines()
                        
            top = []
            bottom = []
            
            for i in range(2):
                temporary_list = raw[i].split('\t')
                if i == 0:
                    incrementer = 0
                    for item in temporary_list:
                        if (("\n" in item) and (incrementer > 0)):
                            top.append(item[:-1].lower())
                        elif (incrementer > 0):
                            top.append(item.lower())
                        incrementer = incrementer + 1
                elif i == 1:
                    incrementer = 0
                    for item in temporary_list:
                        if (("\n" in item) and (incrementer > 0)):
                            bottom.append(float(item[:-1]))
                        elif (incrementer > 0):
                            bottom.append(float(item))
                        incrementer = incrementer + 1    
            
            keys_list.append(filename[:-4])
            all_data[filename[:-4]] = [top, bottom]
            
            infile.close()
        
        except IOError:
            print("file not found")
            
#print(termsToSearchBy)            
for gene in keys_list:
    i = 0
    data = [None]*len(termsToSearchBy)
    for part in termsToSearchBy:
        expression_levels = get_expression(gene, part, all_data)
        data[i] = expression_levels
        i += 1
     
    tsb = []
    for t in termsToSearchBy:
        tsb.append(t)
        
    plt.figure()
    figure = sns.boxplot(data = data)
    figure.set_xticklabels(tsb, rotation=30)
    figure.set_ylabel("Expression Level")
    figure.set_title(species + " " + gene)
    plt.savefig(species + " " + gene, bbox_inches="tight")

    filename = species + "_" + gene
    with open(filename + '.txt', 'w') as outfile:
        outfile.write("species and gene: ")
        outfile.write(species + " " + gene)
        outfile.write("\n")
        h, p = kruskal(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        outfile.write("results from kruskal: ")
        outfile.write("\n")
        outfile.write("h: " + str(h))
        outfile.write("\n")
        outfile.write("p: " + str(p))
        for i in range(len(termsToSearchBy)):
            outfile.write("\n")
            outfile.write("\n")
            outfile.write("condition or part: ")
            outfile.write(termsToSearchBy[i])
            outfile.write("\n")
            outfile.write("# of samples: ")
            outfile.write(str(len(data[i])))              
            outfile.write("\n")
            outfile.write("sample mean: ")
            outfile.write(str(np.mean(data[i])))
            outfile.write("\n")
            outfile.write("standard deviation: ")
            outfile.write(str(np.std(data[i])))
            


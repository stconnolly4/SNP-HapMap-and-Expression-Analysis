# SNP HapMap and Expression Analysis
 
# Use correlation matrix.py to calculate Pearson's Correlation for environmental data. Manually remove environmental variables until no two variables have | r | >= 0.8 . Run correlation matrix.py with the filtered environmental data to find Pearson's Correlation for filtered environmental data.

# Use Tassel 5 to output a CSV of the SNPs and correlations with environmental variables - run a weighted Mixed Linear Model, filter the SNP data to include a site minimum count of 100 and a site minimum allele frequency of 0.02, and use the kinship matrix to account for population structure. Sort the resulting CSV in ascending order of p values. Use calculate_FDR.py to output the SNPs with significantly associated SNPs after False Discovery Rate correction with an alpha value of 0.05. This will output a list of SNPs in a text file; check where the SNPs fall in relation to the genes of interest.

# Download gene expression data from the Medicago truncatula gene expression atlas. Use geneExpression.py to visualize expression - by default, it will search for root, nodule ,shoot, leaf, stem, seed, and myc (myc is related to mycorrhizal fungi).

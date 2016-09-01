# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 23:13:47 2016
@author      : Aldy Rasyid Abe
@description : Feature Extraction with Filter Methods
"""

# Feature Extraction with Filter Methods

import pandas as pd

# Load the data
file = "path/to/file.txt" # "path/to/file.csv"
names = ['step','grid_x','grid_y','grid_z',
        'velocity(0)','velocity(1)','velocity(2)',
        'magnitudes','pressure']
df = pd.read_csv(file, names=names)

"""
Step (1): Calculating the correlation coefficient
"""
# Correlation coefficient scores
pearson_correlation = df.corr(method='pearson')
print(pearson_correlation)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 00:49:00 2018

@author: RikimaruTsui
"""

# Machine Learning A-Z

# Import Library
import numpy as np # maths library
import matplotlib.pyplot as plt 
import pandas as pd # dataset library

# Import the Dataset
dataset = pd.read_csv('Data.csv')

# Create the matrix
X = dataset.iloc[:, :-1].values # take all the column except last one (-1)
y = dataset.iloc[:, 3].values


# Take care of missing data
# SK Learn is the library for data preprocessing
# The Imputer this settings is using Average Strategy ('mean')
from sklearn.preprocessing import Imputer # import the class
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0) # recoginate
imputer = imputer.fit(X[:, 1:3]) # taking colmun 1 to 2 (3 is not been taking) 
X[:, 1:3] = imputer.transform(X[:, 1:3]) # copy the imputered data from imputer to X same positions
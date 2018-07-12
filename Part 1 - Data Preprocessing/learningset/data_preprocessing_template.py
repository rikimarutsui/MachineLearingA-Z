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

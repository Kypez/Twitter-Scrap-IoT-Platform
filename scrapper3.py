# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 10:30:55 2020

@author: Kypez
"""
#Importing libraries and data
import pandas as pd
import re
import numpy as np

#Readind data
iotplatformfinal=pd.read_csv('mindspherecleansed.csv', sep=',', encoding='utf-8')
#print(iotplatformfinal)

#Analysis of the tweet frequency over time
analysis1=iotplatformfinal['year'].value_counts()
print(analysis1)

#Analysis of the frequency of tweets of users
analysis2=iotplatformfinal['username'].value_counts()
print(analysis2)


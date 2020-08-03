# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 15:11:54 2020

@author: petrik
"""

#Importing libraries and data
import pandas as pd
mindsphere=pd.read_csv('mindsphere.csv', sep=';', encoding='utf-8')

#Clearing columns with ireelevant information
mindsphere=mindsphere.drop(columns=['timestamp_epochs','tweet_url'])

#Clearing duplicates and unrelevant weets
mindsphere=mindsphere.drop_duplicates(subset='tweet_id',keep='first')

#adding column with information of the examined hashtag
mindsphere['hashtag']='mindsphere'

#Adding column with year of the tweet
mindsphere['year']=pd.DatetimeIndex(mindsphere['timestamp']).year

#Exporting DataFrames as csv-files
mindsphere.to_csv(r'C:\Users\petrik\Dropbox (Privat)\Python\twitterscraper\mindspherecleansed.csv')

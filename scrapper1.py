# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 14:22:16 2020

@author: petrik
"""

import pandas as pd
from twitterscraper import query_tweets
if __name__ == '__main__':
#print the retrieved tweets to the screen:
#    for tweet in query_tweets("Trump OR Clinton", 10):
#        print(tweet)
        #Or save the retrieved tweets to file:
    file = open("output.csv","w")
    for tweet in query_tweets("mindsphere OR adamos", 10, lang="en"):
        file.write(str(tweet.text.encode('utf-8')))
    file.close()
    
df = pd.read_json('output.csv', encoding='utf-8')
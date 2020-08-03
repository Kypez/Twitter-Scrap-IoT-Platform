# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 21:10:31 2020

@author: Kypez
"""

import pandas as pd
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS as esw
import seaborn as sns
import warnings
from sklearn.decomposition import LatentDirichletAllocation as LDA

#1 Data preparation
iotplatformfinal=pd.read_csv('adamoscleansed.csv', sep=',', encoding='utf-8')
#print(iotplatformfinal)

#2 Clearing unrelevant column
iotplatformfinal=iotplatformfinal.drop(columns=['Unnamed: 0', 'html'], axis=1)
iotplatformfinal['text_processed']=iotplatformfinal['text'].map(
        lambda x: re.sub('[,\.:"!?...-]','',x))
iotplatformfinal['text_processed']=iotplatformfinal['text_processed'].map(
        lambda x: re.sub(r"http\S+\|www\S+|pic.\S+",'',x))
iotplatformfinal['text_processed']=iotplatformfinal['text_processed'].map(
        lambda x: x.lower())
long_string=','.join(list(iotplatformfinal['text_processed'].values))
#print(long_string)

#3 Creating the WordCloud
wordcloud=WordCloud(background_color="white",width=2000,height=2000,stopwords=['mindsphere','rt']+list(STOPWORDS))
wordcloud.generate(long_string)
fig=plt.figure(figsize=(40,30),facecolor='k',edgecolor='k')
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()

#4 Helper function
def plot_10_most_common_words(count_data, count_vectorizer):
    words=count_vectorizer.get_feature_names()
    total_counts=np.zeros(len(words))
    for t in count_data:
        total_counts+=t.toarray()[0]
        
    count_dict=(zip(words, total_counts))
    count_dict=sorted(count_dict,key=lambda x:x[1],reverse=True)[0:10]
    words=[w[0] for w in count_dict]
    counts=[w[1] for w in count_dict]
    x_pos=np.arange(len(words))
    print(words)
    print(counts)
    
    plt.figure(2, figsize=(15, 15/1.6180))
    plt.subplot(title='10 most common words')
    sns.set_context("notebook", font_scale=1.25, rc={"lines.linewidth":2.5})
    sns.barplot(x_pos,counts,palette='husl')
    plt.xticks(x_pos,words,rotation=90)
    plt.xlabel('words')
    plt.ylabel('counts')
    plt.show()
    
#5 Visulaization of the top ten words
count_vectorizer=CountVectorizer(stop_words=['mindsphere','rt']+list(esw))
count_data=count_vectorizer.fit_transform(mindspherefinal['text_processed'])
plot_10_most_common_words(count_data,count_vectorizer)
    
#6 Helper function
def print_topics(model,count_vectorizer,n_top_words):
    words=count_vectorizer.get_feature_names()
    for topic_idx,topic in enumerate(model.components_):
        print("\nTopic #%d:" % topic_idx)
        print("".join([words[i]
              for i in topic.argsort()[:-n_top_words]]))
    
#7 Tweaking the two parameters below
number_topics=3
number_words=12
    
#8 Creating and fitting the LDA model
lda = LDA(n_components=number_topics,n_jobs=-1)
lda.fit(count_data)

#9 Printing the topics found by the LDA model
print("Topics found by the LDA analysis:")
print_topics(lda,count_vectorizer,number_words)

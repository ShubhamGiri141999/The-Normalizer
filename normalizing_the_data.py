#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re, string, unicodedata
import spacy


# In[2]:


import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize


# In[3]:


stop_words = set(stopwords.words('english')) 
nlp = spacy.load('en')


# In[4]:


raw_data = '''''' # enter the content in string format
doc = nlp(raw_data)


# In[5]:


def normalize_the_data(raw_data):
    
    raw_data = raw_data.lower()
    raw_data = re.sub(r'\[.*\]', '', raw_data)
    raw_data = re.sub(r'\(.*\)', '', raw_data)
    raw_data = re.sub(r'\s+', ' ', raw_data)
    raw_data = re.sub(r'\[[0-9]*\]', ' ', raw_data)
    raw_data = re.sub('[^a-zA-Z]', ' ', raw_data)
    raw_data = re.sub('['+string.punctuation+']', '', raw_data).split()
    
    return(raw_data)


# In[6]:


raw_data = normalize_the_data(raw_data)


# In[7]:


print(raw_data) # printing the raw data


# In[8]:


data = ''

for i in raw_data:
    if i not in stop_words:
        data+=(i+' ')


# In[9]:


data # normalized data


# In[10]:


print(doc.ents) # showing entities in the given data


# In[ ]:





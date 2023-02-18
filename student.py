#!/usr/bin/env python
# coding: utf-8

# # Final Project Submission
# 
# Please fill out:
# * Student name: 
# * Student pace: self paced / part time / full time
# * Scheduled project review date/time: 
# * Instructor name: 
# * Blog post URL:
# 

# In[ ]:


#Project Overview
Project Statement
microsoft has decided to create original movie content and created their own movie studio
unfortunely microsoft has no prior knowledge of the movie industry so they dont know how to move forward in creating content.
in this project i will investigate the practices that are foundations for profitable/award wining film

Business Value
A successful movie studio will create a new revenue stream for microsoft
Successful movie studio can improve brand recognition which can in turn help with the promotion/sales of already exisiting products

Methodology
 Analyse past movie data to make recommendations to microsoft on how to be successful in the movie industry
some of the topics i will explore;budgets for high profits and awards, best time to release movie,which actors and directors are most
valuable,which ratings are most profitable by genre.
    


# In[81]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[82]:


movie_gross = pd.read_csv("bom.movie_gross.csv")
movie_gross
            


# In[87]:


movie_gross.isna().any()


# In[88]:


movie_gross.isna().sum()


# In[94]:


movie_gross.dropna(subset=["studio","domestic_gross"], inplace=True)


# In[95]:


movie_gross.isna().sum()


# In[86]:


print('Percentage of Null foreign_gross Values:', len(movie_gross[movie_gross.foreign_gross.isna()])/ len(movie_gross))
print('Number of Unique Cabin Values:', movie_gross.foreign_gross.nunique())


# In[73]:


movie_groz = movie_gross.drop('foreign_gross', axis = 1)
movie_groz.isna().sum()


# In[79]:


domestic_mean = movie_groz['domestic_gross'].mean()
domestic_mean


# movie = movie_groz.dropna()
# movie_groz.isna().sum()

# In[91]:


df = pd.read_csv("ZippedData/imdb.title.ratings.csv.gz")
df


# In[93]:


title = pd.read_csv("ZippedData/imdb.title.basics.csv.gz")
title


# In[18]:


df = pd.read_csv("title.ratings.csv")
df


# In[ ]:





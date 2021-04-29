#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import os
import urllib
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


url = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
file_path = os.path.join("data", "covid")


# In[5]:


os.makedirs(file_path, exist_ok = True)
csv_path = os.path.join(file_path, "WHO-COVID-19-global-data.csv")
urllib.request.urlretrieve(url, csv_path)


# In[6]:


df = pd.read_csv(csv_path)
df


# In[7]:


df_index = df.index
df_index


# In[8]:


df_cols = df.columns
df_cols


# In[9]:


df_index.values


# In[10]:


df.values


# In[12]:


df.dtypes


# In[13]:


df.shape


# In[15]:


df.head(10)


# In[16]:


df.tail(4)


# In[17]:


df.info()


# In[18]:


df.describe()


# In[21]:


df["Country"]


# In[22]:


df["Country"].unique()


# In[23]:


df.Country


# In[24]:


df.Country.unique()


# In[28]:


#df.loc[row_indexer, column_indexer]


# In[29]:


df.loc[1:4, 'Country']


# In[30]:


df.loc[1:8, ['Country', 'New_cases']]


# In[31]:


df.Country == 'United States of America'


# In[32]:


df[df.Country == 'United States of America']


# In[33]:


df[df.New_deaths > 1000]


# In[34]:


df.loc[df.New_deaths > 1000, ['New_deaths', 'Country']]


# In[35]:


df.loc[df.Country_code == 'US', ['New_cases']].max()


# In[36]:


df.loc[df.Country_code == 'US', ['New_cases']].min()


# In[37]:


df.loc[df.Country_code == 'US', ['New_cases']].sum()


# In[38]:


df.loc[df.Country_code == 'US', ['New_deaths']].sum()


# In[39]:


df.loc[df.Country_code == 'US', ['Cumulative_deaths']].max()


# In[40]:


df.New_deaths.idxmax()


# In[41]:


df.loc[df.New_deaths.idxmax()]


# In[43]:


df['percentage_cases'] = (df['New_cases'] / df['Cumulative_cases']) * 100
df


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv("heart.csv")
df.head()


# In[4]:


def find_avgs(binary, continuous):
    '''This function takes the parameters of two columns of the dataframe where col1 is the column of
    binary variables(0 and 1), and col2 is the column of continuous variables. Function returns the mean
    of column2 data based on the two groups in column 1 where the first element returned corresponds to 0
    and the second element corresponds to 1
    '''
    l0 = []
    l1 = []
    for i in range(len(df)):
        if df.loc[i,binary] == 0:
            l0.append(df.loc[i,str(continuous)])
        elif df.loc[i,binary] == 1:
            l1.append(df.loc[i,str(continuous)])
    l0 = pd.Series(l0)
    l1 = pd.Series(l1)
    l0avg = l0.mean()
    l1avg = l1.mean()
    
    return l0avg, l1avg

print("The average maximum heart rate achieved for male: " + str(find_avgs("sex","thalachh")[0]))
print("The average maximum heart rate achieved for female: " + str(find_avgs("sex","thalachh")[1]))
print("The average old peak for male: " + str(find_avgs("sex","oldpeak")[0]))
print("The average old peak for female: " + str(find_avgs("sex","oldpeak")[1]))


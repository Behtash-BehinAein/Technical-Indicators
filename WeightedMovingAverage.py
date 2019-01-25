
# coding: utf-8

# In[1]:


import numpy as np


# In[22]:


def WMA(Vec, Avg_Prd):

    # Initialize
    AVG = np.zeros(Vec.shape[0])
    # Total Sum
    TSUM = sum(range(1, Avg_Prd+1))
    
    for ii in range(Avg_Prd-1, Vec.shape[0]):
        AVG[ii] = sum( Vec[ii-Avg_Prd+1 : ii+1] * np.linspace(1, Avg_Prd, Avg_Prd) )/ TSUM
    return AVG


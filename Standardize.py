
# coding: utf-8

# In[1]:


import numpy as np
import Hull


# In[12]:


def STND(Vec, Avg_prd):
    STND_Vec = np.zeros((Vec.shape[0], ))
    Vec_Avg  = Hull.HMA(Vec,Avg_prd)
    
    for ii in range(Avg_prd, Vec.shape[0]):
        STND_Vec[ii] = ( Vec[ii] - Vec_Avg[ii] )  /  np.std((Vec[ii-Avg_prd: ii]))
    
    
    return STND_Vec


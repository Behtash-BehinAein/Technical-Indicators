
# coding: utf-8

# In[4]:


import numpy as np


# In[3]:


# Sharp ratio is calculated backwards i.e. in a reverse chronological order  

def SharpR(CLOSE, Avg_Prd):
        
    SR = np.zeros(CLOSE.shape[0])
    Return = np.zeros(CLOSE.shape[0])
    STD = np.zeros(CLOSE.shape[0])
   
    Last  =  CLOSE.shape[0] - Avg_Prd + 1
    for ii in range(0, Last):
        ii_reverse = CLOSE.shape[0] - ii
        
        CLOSE_norm = CLOSE[ii_reverse-Avg_Prd : ii_reverse] / CLOSE[ii_reverse-Avg_Prd] 
        Return_Daily    = np.diff(CLOSE_norm) *100
        Return[ii_reverse - 1] = np.mean(Return_Daily) * (252**0.5)
        STD[ii_reverse - 1]   = np.std (Return_Daily) 
        
        SR[ii_reverse - 1] = (Return[ii_reverse - 1]/STD[ii_reverse - 1]) 
                             
    return Return, STD, SR 


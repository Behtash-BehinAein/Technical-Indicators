
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


def Keltner(CLOSE, Avg_Prd, ATR_m, ATR):
    
    KM = np.zeros(CLOSE.shape[0],)
    K = 2/(Avg_Prd+1)
    # N-day exponential moving average --------------------
    # Initialize
    KM[Avg_Prd-1] = sum(CLOSE[:Avg_Prd])/Avg_Prd
    for ii in range(Avg_Prd, CLOSE.shape[0]):
        KM[ii] = KM[ii-1] * (1-K) + CLOSE[ii]*K       # EMA
    KU = KM + ATR_m*ATR
    KL = KM - ATR_m*ATR
    
    return KU, KM, KL    


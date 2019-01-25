
# coding: utf-8

# In[2]:


import numpy as np


# In[1]:


def PC(CLOSE, t0t1, ATR):
    pc = np.zeros(CLOSE.shape[0])
    pc[20:-t0t1] = (CLOSE[20+t0t1 : ] -  CLOSE[20:-t0t1]) / ATR[20:-t0t1]
    return pc  

    '''
    Last  =  CLOSE.shape[0] - t0t1   # The left-over data don't form a whole t0t1 period
    for ii in range(20, Last):
        pc[ii] = (CLOSE[ii+t0t1]  - CLOSE[ii] ) / ATR[ii]
    return pc
    '''
    
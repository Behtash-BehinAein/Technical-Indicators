
# coding: utf-8

# In[1]:


import numpy as np


# In[1]:


def PC(CLOSE, t0t1):
    pc = np.zeros(CLOSE.shape[0])
    pc[:-t0t1] = (CLOSE[t0t1:] - CLOSE[:-t0t1]) /  CLOSE[:-t0t1] * 100 
    return pc
    '''
    Last  =  CLOSE.shape[0] - t0t1   # The left-over data don't form a whole t0t1 period
    for ii in range(0, Last):
        pc[ii] = (CLOSE[ii+t0t1] - CLOSE[ii]) / CLOSE[ii] *100  

    return pc
    '''
    
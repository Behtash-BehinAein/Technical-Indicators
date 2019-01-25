
# coding: utf-8

# In[1]:


import numpy as np
import WeightedMovingAverage


# In[3]:


def HMA(Vec, Avg_Prd):
    Vec1  = 2 *    WeightedMovingAverage.WMA(Vec, int(Avg_Prd/2))
    Vec2  = Vec1 - WeightedMovingAverage.WMA(Vec, Avg_Prd)
    Vec3  =        WeightedMovingAverage.WMA(Vec2, int(np.sqrt(Avg_Prd)))
    return Vec3
    


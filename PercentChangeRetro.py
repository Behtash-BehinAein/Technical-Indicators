# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


def pct_c_ret(VEC, t0t1):
    ret = np.zeros(VEC.shape[0])

    ret[t0t1:] = (VEC[t0t1:] - VEC[:-t0t1])  /  VEC[:-t0t1] * 100 

    return ret


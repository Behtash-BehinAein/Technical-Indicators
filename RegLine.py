
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd


# In[1]:


def RegLine(x,y):
    m = x.shape[0]
    x = x.reshape(m,1)
    # ---------------------
    Bias = np.ones((m,1))
    X = np.hstack((Bias,x))  
    # ---------------------    
    y = y.reshape((m,1))   # Response / indicator
    # ------------------
  
    # Normal Equation to return the parameters for regression line (absolute values)
    Theta = np.matmul(np.matmul(np.linalg.pinv(np.matmul(X.T,X)), X.T), y) 
    Intercept = float(Theta[0])
    Slope = float(Theta[1])   
    
    
    return Intercept, Slope


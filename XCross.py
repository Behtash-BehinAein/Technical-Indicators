
# coding: utf-8

# In[38]:


import numpy as np
import RegLine as RL


# # ![title](img/Intersection of two lines.png)

# In[1]:


def XCross(S1,S2):
    
    # Set both sentiments to 0. 
    # If there is a cross, its sentiment will be adjusted accordingly
    L=0 ;  # Bullish 
    R=0    # Bearish
    
    # Line 1
    x1 = S1[0][0] ; y1 = S1[0][1] 
    x2 = S1[1][0] ; y2 = S1[1][1]
    # Line 2    
    x3 = S2[0][0] ; y3 = S2[0][1]
    x4 = S2[1][0] ; y4 = S2[1][1]
    
    # Denominator
    dnm =  (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if dnm==0:
        X = 0
        XLoc = 0
    else:
        Px = ((x1*y2 - y1*x2) * (x3-x4) - (x1-x2) * (x3*y4 - y3*x4)) / dnm
        Py = ((x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4)) / dnm
        # Check if a cross exists
        if Px < x1 or Px > x2:
            Cross = 0
        else:
            Cross = 1        
        # Check the slope of the fast line      -------------------------------
        # for bullish (L) or bearish (R) cross  ------------------------------- 
        Int, Slp = RL.RegLine(np.array([x1,x2]), np.array([y1,y2]))
        if Slp > 0:
            L=1;
        else:
            R=-1;
        # Note: Reg line was not used for the cross point because it is only
        # an approximation. The actual data was used to detect a cross
        # --------------------------------------------------------------------- 
        X = Cross*L + Cross*R    
        XLoc = Cross*Py
    return X, XLoc   


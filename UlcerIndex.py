
# coding: utf-8

# In[ ]:


import numpy as np 


# In[ ]:


def UI(CLOSE, Avg_Prd):
    UI_L = np.zeros(CLOSE.shape[0],)
    UI_S = np.zeros(CLOSE.shape[0],)
    
    for ii in range(Avg_Prd-1, CLOSE.shape[0]):
        
        Squared_Retracement_L = 0
        Squared_Retracement_S = 0
        for jj in range(1, Avg_Prd+1):
            PriceMAX = np.max(CLOSE[ii-Avg_Prd+1 : (ii-Avg_Prd+1) + jj]) 
             
            PriceMIN = np.min(CLOSE[ii-Avg_Prd+1 : (ii-Avg_Prd+1) + jj]) 
            
            if CLOSE[(ii-Avg_Prd+1) + (jj-1)] < PriceMAX:
                Squared_Retracement_L += (  (PriceMAX - CLOSE[(ii-Avg_Prd+1) + (jj-1)])  / PriceMAX  )**2    
            if CLOSE[(ii-Avg_Prd+1) + (jj-1)] > PriceMIN:
                Squared_Retracement_S += (  (CLOSE[(ii-Avg_Prd+1) + (jj-1)] - PriceMIN) / PriceMIN   )**2 
            
        
        UI_L[ii] = 100* np.sqrt(Squared_Retracement_L / Avg_Prd)
        UI_S[ii] = 100* np.sqrt(Squared_Retracement_S / Avg_Prd)

    return UI_L, UI_S 


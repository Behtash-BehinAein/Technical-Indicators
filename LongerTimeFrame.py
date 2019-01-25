
# coding: utf-8

# In[212]:


import numpy as np
import pandas as pd


# In[293]:


def LTF(WEEKDAY, OPEN, HIGH, LOW, CLOSE):  # L_Prd: 5 for weekly, 30 for monthly, or some other number    
 
    WOPEN   = np.zeros(CLOSE.shape[0],)
    WHIGH   = np.zeros(CLOSE.shape[0],)
    WLOW    = np.zeros(CLOSE.shape[0],)
    WCLOSE  = np.zeros(CLOSE.shape[0],)
    
    
    # ==========================================================================================================
    # Count the number of days in each trading week taking into acount market holidays
    
    # Set the intial day count to 1. This will be reset for each new week
    D_COUNT = 1

    # Week index and the number of days in that week
    W_NoDays =  pd.DataFrame(columns=['No Days in the Week'])    

    for dd in range(CLOSE.shape[0]):
        #print(dd)

        # Count the number of days in the current week ------------------------------------------------------
        if dd+1 < CLOSE.shape[0]: 
            if WEEKDAY[dd] < WEEKDAY[dd+1]:
                D_COUNT += 1
            # If a new week starts, add to the count of weeks and reset the number of days in the week to 1
            else :
                W_NoDays = W_NoDays.append({'No Days in the Week': D_COUNT}, ignore_index=True)
                #print('D_COUNT:', D_COUNT)
                D_COUNT  = 1      
        else:  
                if WEEKDAY[dd] > WEEKDAY[dd-1]:
                    W_NoDays = W_NoDays.append({'No Days in the Week': D_COUNT}, ignore_index=True)
                else: 
                    W_NoDays = W_NoDays.append({'No Days in the Week': 1}, ignore_index=True)
    # ==========================================================================================================

    
    for ww in range(0, W_NoDays.shape[0]-1):
        
        Start0 = int(np.sum(W_NoDays[:ww]))
        End0   = int(np.sum(W_NoDays[:ww+1]))    

        Start1 = End0
        End1   = int(np.sum(W_NoDays[:ww+2]))    
    
        # Since the first week will be effectively set to 0, there is no lag for the 1st weel. All other weeks
        # will report the data of the previous week
        if ww==0:
            WOPEN [Start0: End0]  = OPEN[Start0]
            WCLOSE[Start0: End0]  = CLOSE[End0-1]
            WHIGH[Start0: End0]   = max(HIGH[Start0: End0])
            WLOW[Start0: End0]    = min(LOW [Start0: End0])            
        
        # There is a lag of one week here
        WOPEN [Start1: End1]  = OPEN[Start0]
        WCLOSE[Start1: End1]  = CLOSE[End0-1]
        WHIGH[Start1: End1]   = max(HIGH[Start0: End0])
        WLOW[Start1: End1]    = min(LOW [Start0: End0])
    
    
    
    return  WOPEN, WHIGH, WLOW, WCLOSE, W_NoDays


# In[294]:


'''
# Test and diagnostics 

Curated = 'C:/Users/Behtash Behin-Aein/Desktop/iStorage/MKT/Analysis/StatsTechnicalsFeatures/Curated Data'

Security = pd.read_csv(Curated+'/'+'A.csv')
Security = Security.reset_index(drop=True)

# Price and Volume --------------------
WEEKDAY = np.array(Security['WEEKDAY'])
OPEN    = np.array(Security['OPEN'])
HIGH    = np.array(Security['HIGH'])
LOW     = np.array(Security['LOW'])
CLOSE   = np.array(Security['CLOSE'])
#VOLUME  = np.array(Security['VOLUME'])
# -------------------------------------

'''


# In[295]:


'''
WOPEN, WHIGH, WLOW, WCLOSE, W_NoDays   = LTF(WEEKDAY, OPEN, HIGH, LOW, CLOSE)
'''


# In[298]:


'''
WCLOSE[:20]
'''


# In[296]:


'''
WCLOSE[:20]
'''


# In[299]:


'''
WHIGH[-10:]
'''


# In[300]:


'''
WHIGH[-10:]
'''


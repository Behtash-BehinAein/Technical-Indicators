
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import LBR3_10Oscillator
import LongerTimeFrame


# In[79]:


# Test and diagnostics 
'''
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


# In[80]:


'''
WOPEN, WHIGH, WLOW, WCLOSE, W_NoDays   = LongerTimeFrame.LTF(WEEKDAY, OPEN, HIGH, LOW, CLOSE)
'''


# In[75]:


def ImpulseW(WCLOSE, W_NoDays, Avg_Prd):
    
    # Sampling at a lower variable frequency ---------------------------------------------
    # Unique weekly values for differential week-to-week calculations are calculated here 
    # from weekly values reported on daily basis
    
    wclose = np.zeros((W_NoDays.shape[0]))  
    counter = 0
    for ww in range(wclose.shape[0]):
        
        wclose[ww] = WCLOSE[W_NoDays.iloc[ww][0]+counter-1]
        counter   +=  W_NoDays.iloc[ww][0]
        #print(counter)
    # ====================================================================================
    
           
    EMA = np.zeros(wclose.shape[0],)
    K = 2/(Avg_Prd+1)
    # N-ticks exponential moving average --------------------

    # Initialize
    EMA[Avg_Prd] = sum(wclose[:Avg_Prd])/Avg_Prd
    for ii in range(Avg_Prd+1, wclose.shape[0]):
        EMA[ii] = EMA[ii-1] * (1-K) + wclose[ii]*K       # Weekly EMA of closing prices
    
    
    EMA[:Avg_Prd]   = wclose[:Avg_Prd]
    # Instantiate LBR 3-10 Oscillator -----------------------
    [ThreeTenF, ThreeTenF_Slp, ThreeTenS, ThreeTenS_Slp, ThreeTenHist_Slp ]    = LBR3_10Oscillator.LBR310(wclose) 
    #--------------------------------------------------------
    
    # Differentials Unique --------------------------------------
    EMA_Slp_unique         = np.zeros(EMA.shape[0])
    EMA_Slp_unique[1:]     = np.diff(EMA)/EMA[:-1]*100
    #==
    LBR310Hist_Slp_unique      = np.zeros(ThreeTenF.shape[0])
    LBR310Hist_Slp_unique[1:]  = np.diff(ThreeTenF - ThreeTenS)
    # -----------------------------------------------------------
    
    # Sample to higher frequency based on the number of days in each week  -------
    EMA_Slp_RepW        = np.zeros(WCLOSE.shape[0],)    
    LBR310Hist_Slp_RepW = np.zeros(WCLOSE.shape[0],)    
    
    for ww in range(Avg_Prd, W_NoDays.shape[0]):
        Start = int(np.sum(W_NoDays[:ww]))
        End   = int(np.sum(W_NoDays[:ww+1])) 
        
        #print(End)
        EMA_Slp_RepW[Start: End]        = EMA_Slp_unique[ww]
        #print(EMA_Slp_RepW[Start: End])
        LBR310Hist_Slp_RepW[Start: End] = LBR310Hist_Slp_unique[ww]
    # ----------------------------------------------------------------------------    
    
    
       
    # Calculate impulse ----------------------------------
    '''    
    IMPW_tmp = np.zeros(EMA_Slp_unique.shape[0]-1,)
    for ii in range(Avg_Prd, EMA_Slp_unique.shape[0]-1):
        if   EMA_Slp_unique[ii] >0 and LBR310_Slp_unique[ii] >0:
            IMPW_tmp[ii] = 1
        elif EMA_Slp_unique[ii] <0 and LBR310_Slp_unique[ii] <0:
            IMPW_tmp[ii] = -1

    # ----------------------------------------------        
    # Calculate impulse for the left-over ticks
    IMPW = np.zeros(5*IMPW_tmp.shape[0], )
    for ii in range(Avg_Prd, IMPW_tmp.shape[0]): 
        IMPW[5*ii : 5*ii+5] = np.array(5*[ IMPW_tmp[ii] ])
        
        
    # Calculate Impulse for the left_over ticks
    if   EMA_Slp_unique[-1] >0 and LBR310Hist_Slp_unique[-1] >0:
        Last_Imp = 1
    elif EMA_Slp_unique[-1] <0 and LBR310Hist_Slp_unique[-1] <0:
        Last_Imp = -1
    else:  
        Last_Imp = 0
    # ----------------------------------------------
    None_Whole_Tikcs = [Last_Imp] * Left_Over 
    IMPW = np.hstack((IMPW, np.array(None_Whole_Tikcs)))
     '''   
    return EMA_Slp_RepW, LBR310Hist_Slp_RepW #IMPW

    


# In[78]:


'''
EMA_Slp_RepW, LBR310Hist_Slp_RepW  = ImpulseW(WCLOSE, W_NoDays, 13)
'''


# In[77]:


'''
EMA_Slp_RepW[-10:]
'''


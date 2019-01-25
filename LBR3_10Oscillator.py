
# coding: utf-8

# In[1]:


import numpy as np
import XCross as XC
import RegLine as RL
import Hull


# In[3]:


def LBR310(CLOSE):
    
    ThreeTenF        = np.zeros(CLOSE.shape[0], )
    ThreeTenS        = np.zeros(CLOSE.shape[0], )
    ThreeTenF_Slp    = np.zeros(CLOSE.shape[0], )
    ThreeTenS_Slp    = np.zeros(CLOSE.shape[0], )
    ThreeTenHist     = np.zeros(CLOSE.shape[0], )
    ThreeTenHist_Slp = np.zeros(CLOSE.shape[0], )    
    #ThreeTenF_X_0 = np.zeros(CLOSE.shape[0],)
    #ThreeTenF_X_ThreeTenS = np.zeros(CLOSE.shape[0],)
    #ThreeTenF_X_ThreeTenS_Loc = np.zeros(CLOSE.shape[0],)
    
    Cross_x  = np.array((1,2))  
    Reg_x    = np.array((1,2,3)) 
    
    for ii in range(9, CLOSE.shape[0]):
        SMA10 = np.mean(CLOSE[ii-10+1: ii+1])
        SMA3 =  np.mean(CLOSE[ii-3+1 : ii+1])
        ThreeTenF[ii] = (SMA3 - SMA10)         # Fast Line
        
        # Fast slope          -----------------------------------------
        # Based on 3-tick regression line 
        Reg_y = ThreeTenF[ii-3+1:ii+1]
        Intercept, Slope = RL.RegLine(Reg_x,Reg_y)
        ThreeTenF_Slp[ii] = Slope
        '''        
        # Fast crosses 0     -----------------------------------------
        S1 = ((Cross_x[0], ThreeTenF[ii-1]), (Cross_x[1], ThreeTenF[ii])) 
        S2 = ((Cross_x[0], 0), (Cross_x[1], 0))  
        ThreeTenF_X_0[ii], ThreeTenF_X_0_Loc  = XC.XCross(S1, S2) 
        '''
    for ii in range(26, CLOSE.shape[0]):            
        ThreeTenS[ii] = np.mean(ThreeTenF[ii-16:ii])   # Slow Line
        
        # Slow slope          -------------------------------------------
        # Based on 3-tick regression line 
        Reg_y = ThreeTenS[ii-3+1:ii+1]
        Intercept, Slope = RL.RegLine(Reg_x,Reg_y)
        ThreeTenS_Slp[ii] = Slope       
        '''        
        # Fast crosses slow  (Bullish/Bearish) Cross   ------------------
        S1 = ((Cross_x[0], ThreeTenF[ii-1]), (Cross_x[1], ThreeTenF[ii])) 
        S2 = ((Cross_x[0], ThreeTenS[ii-1]), (Cross_x[1], ThreeTenS[ii]))  
        ThreeTenF_X_ThreeTenS[ii], ThreeTenF_X_ThreeTenS_Loc[ii]  = XC.XCross(S1, S2)
        # Cross quality -----------------------------------------------
        if ThreeTenF_X_ThreeTenS[ii]      ==  1:
            ThreeTenF_X_ThreeTenS_Loc[ii] = (ThreeTenF_X_ThreeTenS_Loc[ii] < 0) * ThreeTenF_X_ThreeTenS_Loc[ii] 
            ThreeTenF_X_ThreeTenS[ii]     = (ThreeTenF_X_ThreeTenS_Loc[ii] < 0) 

        if ThreeTenF_X_ThreeTenS[ii]      == -1:
            ThreeTenF_X_ThreeTenS_Loc[ii] = (ThreeTenF_X_ThreeTenS_Loc[ii] > 0) * ThreeTenF_X_ThreeTenS_Loc[ii] 
            ThreeTenF_X_ThreeTenS[ii]     = (ThreeTenF_X_ThreeTenS_Loc[ii] > 0) *-1
        # -------------------------------------------------------------              

        '''
        
    #ThreeTenSmooth = Hull.HMA(ThreeTenF, 5)
    ThreeTenHist   = ThreeTenF - ThreeTenS
    for ii in range(26, CLOSE.shape[0]):
        Reg_y = ThreeTenHist[ii-3+1:ii+1]  # For 3-tick Regression-Line
        Intercept, ThreeTenHist_Slp[ii] = RL.RegLine(Reg_x,Reg_y)
        
        
    return ThreeTenF, ThreeTenF_Slp, ThreeTenS, ThreeTenS_Slp, ThreeTenHist_Slp #,ThreeTenF_X_ThreeTenS, ThreeTenF_X_ThreeTenS_Loc, ThreeTenHist
     


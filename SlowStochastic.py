
# coding: utf-8

# In[249]:


import numpy as np
import XCross as XC     # User function that checks the existence and location of a crossing point between two line segments  
import RegLine as RL    # User function that fits a regression line to the past N-ticks (N is an input parameter) 


# In[1]:


def SlowStk(CLOSE, HIGH, LOW, Look_Prd, Avg_Prd1, Avg_Prd2):
    
    Pct_Kf     = np.zeros(CLOSE.shape[0],)
    Pct_Ks     = np.zeros(CLOSE.shape[0],)
    Pct_Ks_Slp = np.zeros(CLOSE.shape[0],)
    Pct_D      = np.zeros(CLOSE.shape[0],)    
    Pct_D_Slp  = np.zeros(CLOSE.shape[0],)    

    
    Ln = np.zeros(CLOSE.shape[0],)
    Hn = np.zeros(CLOSE.shape[0],)
    '''
    F_X_20 = np.zeros(CLOSE.shape[0],)
    F_X_80 = np.zeros(CLOSE.shape[0],)
    F_X_S  = np.zeros(CLOSE.shape[0],)
    F_X_S_Loc = np.zeros(CLOSE.shape[0],)
    '''
    Cross_x  = np.array((1,2))  
    Reg_x  = np.array((1,2,3)) 

    # Calculate %K of fast stochastic ----------------
    for ii in range(Look_Prd-1, CLOSE.shape[0]):
        Ln[ii] = min(LOW [ii-Look_Prd+1: ii+1])
        Hn[ii] = max(HIGH[ii-Look_Prd+1: ii+1])
    #    Pct_Kf[ii] =  (CLOSE[ii] - Ln[ii]) / (Hn[ii] - Ln[ii])  - 0.5     # CH 100* and -0.5
    
    # Calculate %K of slow stochastic -------------------------------------------------------
    for ii in range(Look_Prd+Avg_Prd1, CLOSE.shape[0]):
        Pct_Ks[ii] = (sum(CLOSE[ii-Avg_Prd1+1 : ii+1] - Ln[ii-Avg_Prd1+1 : ii+1]) /        sum(Hn[ii-Avg_Prd1+1 : ii+1] - Ln[ii-Avg_Prd1+1 : ii+1])  - 0.5) *2  #CH: 100* -->  -0.5, *2

        # Fast slope          -----------------------------------------
        # Based on 3-tick regression line 
        Reg_y = Pct_Ks[ii-3+1:ii+1]
        Intercept, Slope = RL.RegLine(Reg_x,Reg_y)
        Pct_Ks_Slp[ii] = Slope
        '''
        # Fast crosses "20"     -----------------------------------------
        # 20 becomes -0.6 if SS is normalized to (-1,1)
        S1 = ((Cross_x[0], Pct_Ks[ii-1]), (Cross_x[1], Pct_Ks[ii])) 
        S2 = ((Cross_x[0], -0.6), (Cross_x[1], -0.6))  
        F_X_20[ii], F_X_20_Loc  = XC.XCross(S1, S2) 
        # Fast crosses "80"     -----------------------------------------
        # 80 becomes 0.6 if SS is normalized to (-1,1)
        S1 = ((Cross_x[0], Pct_Ks[ii-1]), (Cross_x[1], Pct_Ks[ii])) 
        S2 = ((Cross_x[0], 0.6), (Cross_x[1], 0.6))          
        F_X_80[ii], F_X_80_Loc = XC.XCross(S1, S2)       
        '''
        
    # Calculate %D of slow stochastic ---------------------------------
    for ii in range(Look_Prd+Avg_Prd1+Avg_Prd2 , CLOSE.shape[0]):
        Pct_D[ii] = sum(Pct_Ks[ii-Avg_Prd2+1 : ii+1]) / Avg_Prd2

        # Slow slope          -----------------------------------------
        # Based on 3-tick regression line 
        '''
        Reg_y = Pct_D[ii-3+1:ii+1]
        Intercept, Slope = RL.RegLine(Reg_x,Reg_y)
        Pct_D_Slp[ii] = Slope       

        # Fast crosses slow: Bullish/Bearish Cross   ------------------
        S1 = ((Cross_x[0], Pct_Ks[ii-1]), (Cross_x[1], Pct_Ks[ii])) 
        S2 = ((Cross_x[0], Pct_D[ii-1]),  (Cross_x[1], Pct_D[ii]))  
        F_X_S[ii], F_X_S_Loc[ii]  = XC.XCross(S1, S2)
        # F_X_S:     identir for bullish (1) or bearish (-1) cross
        # F_X_S_Loc: location of the cross
        # Cross quality -----------------------------------------------
        # Bullish Cross
        if F_X_S[ii] ==  1:
            F_X_S_Loc[ii] = (F_X_S_Loc[ii] < 0) * F_X_S_Loc[ii] 
            F_X_S[ii]     = (F_X_S_Loc[ii] < 0) 
        # Bearish Cross
        if F_X_S[ii] == -1:
            F_X_S_Loc[ii] = (F_X_S_Loc[ii] > 0) * F_X_S_Loc[ii] 
            F_X_S[ii]     = (F_X_S_Loc[ii] > 0) *-1     
        '''
        # -------------------------------------------------------------
     
    # Repeat the existence of a cross for 3-ticks if there are no new crosses
    # Override the old cross with the new one if there is a new cross within 3-ticks
    '''    
    X1 = np.hstack(( 0     , F_X_S[0:-1])) 
    X2 = np.hstack(([0,0]  , F_X_S[0:-2])) 
    X3 = np.hstack(([0,0,0], F_X_S[0:-3])) 
    
    A =  np.array(F_X_S).astype(int)
    B =  np.array(X1).astype(int)
    C =  np.array(X2).astype(int)
    D =  np.array(X3).astype(int)
    
    R1 = A^B
    R1[abs(R1)==2] = A[abs(R1)==2]
    R1[A==B] = A[A==B]
    R1 = np.sign(R1)
    
    R2 = R1^C
    R2[abs(R2)==2] = R1[abs(R2)==2]
    R2[R1==C] = R1[R1==C]
    R2 = np.sign(R2)
    
    R3 = R2^D
    R3[abs(R3)==2] = R2[abs(R3)==2]
    R3[R2==D] = R2[R2==D]
    R3 = np.sign(R3)
       
    F_X_S = R2
    '''
    
    # ------------------------------------------------------------------
    
    return Pct_Ks, Pct_Ks_Slp, Pct_D  #, F_X_20, F_X_80, F_X_S, F_X_S_Loc  Pct_D_Slp 


# In[340]:


'''
# Tests and diagnostics 

A = np.array([1 , -1, 1, -1,  0])
B = np.array([0 , 1, -1,  1, -1])
C = np.array([0 , 0,  1, -1,  1])
D = np.array([0 , 0,  0,  1, -1])

A = np.array([1 , 0, 0, 0, 0])
B = np.array([0 , 1, 0, 0, 0])
C = np.array([0 , 0, 1, 0, 0])
D = np.array([0 , 0, 0, 1, 0])


R1 = A^B
R1[abs(R1)==2] = A[abs(R1)==2]
R1[A==B] = A[A==B]
R1 = np.sign(R1)
#R1


R2 = R1^C
R2[abs(R2)==2] = R1[abs(R2)==2]
R2[R1==C] = R1[R1==C]
R2 = np.sign(R2)



R3 = R2^D
R3[abs(R3)==2] = R2[abs(R3)==2]
R3[R2==D] = R2[R2==D]
R3 = np.sign(R3)

R3
'''


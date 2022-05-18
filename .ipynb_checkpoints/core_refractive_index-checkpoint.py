import numpy as np
import scipy.special as sp

ai_cl = [0.6961663,0.4079426, 0.8974794]
Wli_cl = [0.068404, 0.1162414,9.896161]
Wl_cl = 1

def sellmier(Ai, wli, wl):
    import numpy as np
    n = 0
    for i in range(0,len(Ai)):
        suma = Ai[i]* ((wl ** 2) / ((wl ** 2) - (wli[i] **2)))
        n = suma + n
        
    n = np.sqrt(1+n)
    return n

def n_cladding():
    ai_cl = [0.6961663,0.4079426, 0.8974794]
    Wli_cl = [0.068404, 0.1162414,9.896161]
    Wl_cl = 1
    ncl_e = sellmier(ai_cl, Wli_cl,Wl_cl)
    return ncl_e
    
    

def n_core():
    nco = 1.4568527308462205
    return nco


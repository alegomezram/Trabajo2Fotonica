import numpy as np

def n_core():
    A, wl = [0.6867178, 0.4348151, 0.8965658], [0.0726752, 0.1151435 , 10.002398]
    n = 0
    for i in range(0,len(A)):
        suma = A[i]* (((1300 * (10 ** -9)) ** 2) / (((1300 * (10 ** -9))**2) - ((wl[i] * (10 ** -6))**2)))
        n = suma + n
        
    nco = np.sqrt(1+n)
        
    return nco


def Newton(func, *args):
    
    import numpy as np
            
    for i in args:
        point = i
        g = func(i) #funcion
        dgx = (np.diff([func(i+0.0000000001),func(i-0.0000000001)])/np.diff([i+0.0000000001,i-0.0000000001]))[0] #derivada

    it = point - (g/dgx)
            
    proof = round(func(it),10)
            
    if proof == 0:
        return it
    else:
        return Newton(func,it)
    
    
def Biseccion(func, *args):
    
    import numpy as np

    for i in args:
        a = i[0]
        b = i[1]
        p = (i[0]+i[1])/2
        f_1 = func(a)
        f_2 = func(b)
        f_p = func(p)
        
    proof = round(f_1*f_p,20)
    #print(proof)
    if proof == 0:
        return p
    elif proof < 0:
        return Biseccion(func,[a,p])
    else:
        return Biseccion(func,[p,b])
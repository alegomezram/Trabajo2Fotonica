#fraccion de funciones de Bessel de primer tipo
def tm_te_01(beta):
    a = 4.1 * (10 ** -6)
    tm_te_equation = q1(beta) * ((sp.jv(0,q1(beta)*a)) / ( sp.jv(1,q1(beta)*a)))
    return tm_te_equation

#fraccion de funciones de Bessel de segundo tipo modificadas

def tm_te_02(beta):
    a = 4.1 * (10 ** -6)
    tm_te_equation = -q2(beta) * ((sp.kn(0,q2(beta)*a)) / (sp.kn(1,q2(beta)*a)))
    return tm_te_equation


#Ecuación de dispersion mods TE y TM

def tm_te(beta):
    tm_te_equation = tm_te_01(beta) - tm_te_02(beta)
    return tm_te_equation



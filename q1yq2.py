import numpy as np
from core_refractive_index import *

nco = n_core() #indice de refracción del nucleo
ncl =  1.4527 #indice de refracción del revestimiento
ko = (2*np.pi)/(10 ** -6) #numero de onda para longitud de onda de un micrometro

#funciones q1 y q2 que contienen la velocidad de propagacion y aparecen en las funciones de Bessel

def q1(beta):
    q1_equation = np.sqrt((nco ** 2)*(ko ** 2) - (beta ** 2))
    return q1_equation

def q2(beta):
    q2_equation = np.sqrt(-(ncl ** 2)*(ko ** 2) + (beta ** 2))
    return q2_equation





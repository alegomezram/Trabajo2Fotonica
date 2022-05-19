import numpy as np
import scipy.special as sp
from core_refractive_index import *
from q1yq2 import *


def EH_01(v,beta):
    a = 4.1 * (10 ** -6)
    EH_01_equation = q1(beta) * ((sp.jv(v,q1(beta)*a))   /   (sp.jv(v+1,q1(beta)*a)))
    return EH_01_equation

def EH_02(v, beta):
    a = 4.1 * (10 ** -6)
    EH_02_equation = -q2(beta) * ((sp.kn(v,q2(beta)*a))   /   (sp.kn(v+1,q2(beta)*a)))
    return EH_02_equation

def EH(v,beta):
    EH_equation = EH_01(v, beta) - EH_02(v, beta)
    return EH_equation



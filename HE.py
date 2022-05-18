import numpy as np
import scipy.special as sp
from core_refractive_index import *
from q1yq2 import *

def HE_01(v, beta):
    a = 4.1 * (10 ** -6)
    HE_01_equation = q1(beta) * ((sp.jv(v,q1(beta)*a))   /   (sp.jv(v-1,q1(beta)*a)))
    return HE_01_equation

def HE_02(v, beta):
    a = 4.1 * (10 ** -6)
    HE_02_equation = q2(beta) * ((sp.kn(v,q2(beta)*a))   /   (sp.kn(v-1,q2(beta)*a)))
    return HE_02_equation


def HE(v,beta):
    HE_equation = HE_01(v, beta) - HE_02(v, beta)
    return HE_equation


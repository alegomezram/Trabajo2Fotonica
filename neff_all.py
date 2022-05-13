import numpy as np
import scipy.special as sp
import scipy.optimize as sp2
import pandas as pd
from core_refractive_index import *
from q1yq2 import *
from TE_TM import *
from Zeros import *

tm_te_zeros = sp2.bisect(tm_te,9.1276,9.130570)

df =  pd.DataFrame()
df['neff modos Te y TM'] = [tm_te_zeros]
df.to_csv('Data/Data.csv')
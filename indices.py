#índices de refracción para una fibra Corning SMF-28

import matplotlib.pyplot as plt
import numpy as np

#unidades en um
Ai=[0.688021905882353, 0.433983641176471, 0.896512229411764]
w_length_i=[0.071982852941176, 0.115749847058824, 9.996148823529410]
w_length=1

ni=0
#n sílice
for i in range(0,3,1):

	ni=Ai[i]*((w_length**2)/((w_length**2)-(w_length_i[i]**2)))+ni

nsi=np.sqrt(1+ni) 

print(nsi)

nge=nsi+1.4145*(10**(-3))

print(nge)

clc, close all, clear all


a=8.2;                     %radius in um
n1=1.4568527308462205;     %core
n2=1.4504;                 %cladding

q1=np.sqrt((n1^2)*(k^2)-(beta^2));
q2=np.sqrt((beta^2)-(n2^2)*(k^2));

q1*(sp.jv(0,q1*a)/sp.jv(1,q1*a))+q2*(sp.kn(0,q2*a)/sp.kn(1,q2*a))=0
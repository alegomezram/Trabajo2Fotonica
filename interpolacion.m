clc, close all, clear all

format long

X=[4.1 5.8];
Ya1=[0.6867178 0.7088876];
Ya2=[0.4348151 0.4206803];
Ya3=[0.8965658 0.8956551];
Yl1=[0.0726752 0.0609053];
Yl2=[0.1151435 0.1254514];
Yl3=[10.002398 9.896162];

Ai=[];
[A]=lagran(X,Ya1);
Ai(1)=polyval(A,4.2);
[B]=lagran(X,Ya2);
Ai(2)=polyval(B,4.2);
[C]=lagran(X,Ya3);
Ai(3)=polyval(C,4.2);

w_length_i=[];
[A]=lagran(X,Yl1);
w_length_i(1)=polyval(A,4.2);
[B]=lagran(X,Yl2);
w_length_i(2)=polyval(B,4.2);
[C]=lagran(X,Yl3);
w_length_i(3)=polyval(C,4.2);

w_length=1
ni=0;
for i=1:3
    ni=Ai(i)*((w_length^2)/((w_length^2)-(w_length_i(i)^2)))+ni
end
nge=sqrt(1+ni) 



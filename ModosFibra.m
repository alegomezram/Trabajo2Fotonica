clc, close all, clear all

%Parámetros
%Todas las unidades en um
lambda=1;               %longitud de onda
k0=2*pi/lambda;         %numero de onda
a=4.1;                  %radius in um
n1=1.4568527308462205;  %core (germanio)
n2=1.450417399464332;   %cladding (sílice)

% syms beta
% q1=sqrt((n1^2)*(k0^2)-(beta^2));
% q2=sqrt((beta^2)-(n2^2)*(k0^2));
% 
% j0=besselj(0,q1*a);
% j1=besselj(0,q1*a);
% k0=besselk(0,q2*a);
% k1=besselk(1,q2*a);
% 
% f=q1.*(j0./j1)+q2.*(k0./k1);

% Plot
R=@(beta) (sqrt((n1^2)*(k0^2)-(beta.^2))).*((besselj(0,(sqrt((n1^2)*(k0^2)-(beta.^2)))*a))./(besselj(1,(sqrt((n1^2)*(k0^2)-(beta.^2)))*a)));
S=@(beta) -(sqrt((beta.^2)-(n2^2)*(k0^2))).*((besselk(0,(sqrt((beta.^2)-(n2^2)*(k0^2)))*a))./(besselk(1,(sqrt((beta.^2)-(n2^2)*(k0^2)))*a)));
beta=linspace(n2*k0,n1*k0,1000);
figure('Name','Modos TE'), plot(beta,R(beta),beta,S(beta),'LineWidth',1.5), grid on
legend('R','S','Location','best')
title('Modos TE pares')
xlabel('beta [rad]') 
ylabel('R(θ),S(θ)')

% Método de Newton para hallar las soluciones (intersecciones de las gráficas)
% df = diff(f)
% f=@(beta) (sqrt((n1^2)*(k0^2)-(beta.^2))).*((besselj(0,(sqrt((n1^2)*(k0^2)-(beta.^2)))*a))./(besselj(1,(sqrt((n1^2)*(k0^2)-(beta.^2)))*a)))+(sqrt((beta.^2)-(n2^2)*(k0^2))).*((besselk(0,(sqrt((beta.^2)-(n2^2)*(k0^2)))*a))./(besselk(1,(sqrt((beta.^2)-(n2^2)*(k0^2)))*a)));
% df=@(beta) (beta.*besselk(0, (41*(beta.^2 -5844206315499461/70368744177664)^(1/2))/10))/((beta.^2 - 5844206315499461/70368744177664)^(1/2)*besselk(1, (41*(beta.^2 - 5844206315499461/70368744177664)^(1/2))/10)) - beta./(1474045368996815/17592186044416 - beta.^2)^(1/2) - (41*beta)./10 + ((beta.^2 - 5844206315499461/70368744177664)^(1/2)*besselk(0, (41*(beta.^2 - 5844206315499461/70368744177664)^(1/2))/10)*((beta.*besselk(1, (41*(beta.^2 - 5844206315499461/70368744177664)^(1/2))/10))/(beta.^2 - 5844206315499461/70368744177664) + (41*beta.*besselk(0, (41*(beta.^2 - 5844206315499461/70368744177664)^(1/2))/10))/(10*(beta.^2 - 5844206315499461/70368744177664)^(1/2))))/besselk(1, (41*(beta.^2 - 5844206315499461/70368744177664)^(1/2))/10)^2;
% p0= 10;
% delta=1e-10;
% epsilon=1e-9;
% max=80;
% [p0, err, k, y] = newton(f, df, p0, delta, epsilon, max) 
% '---'
% [c, err, yc] = bisect (f, n2*k0, n1*k0, delta)

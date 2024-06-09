import numpy as np
import matplotlib.pyplot as plt
import control as co
from scipy import signal
# PARAMETROS
m = 0.2      # massa da haste em Kg
l = 0.3      # comprimento ate o centro de gravidade em m
M = 0.8      # massa do carro em Kg
I = 0.006    # momento de inercia da haste em Kg.m^2
g = 9.80665  # aceleracao da gravidade em m^2
# THETA(s)/U(s)
b0 = m*l
a0 = (m*l)**2 - (M + m)*(I + m*(l**2))
a1 = 0
a2 = (M + m)*m*g*l
# Numerador e denominador da FT (THETA/U)
num_haste_theta_u = [0,  0, b0/a0]
den_haste_theta_u = [1, a1/a0, a2/a0]
r1, p1, k1 = signal.residue(num_haste_theta_u, den_haste_theta_u)
print('Resíduos, Polos e termo direto:')
print(r1, p1, k1)
# FT
Gs1 = co.tf(num_haste_theta_u, den_haste_theta_u)
Gs1x = signal.TransferFunction(num_haste_theta_u, den_haste_theta_u)
print(Gs1)
p1, z1 = co.pzmap(Gs1, plot=True, grid=True, title='Pole Zero Map THETA/U')
print('Polos e zeros:')
print(p1, z1)
# X(s)/U(s)
b0 = -(I + m*(l**2))
b1 = 0
b2 = m*g*l
a0 = (m*l)**2 - (M + m)*(I + m*(l**2))
a1 = 0
a2 = (M + m)*m*g*l
a3 = 0
a4 = 0
# Numerador e denominador da FT (X/U)
num_haste_x_u = [b0/a0, b1/a0, b2/a0]
den_haste_x_u = [1, a1/a0, a2/a0, a3/a0, a4/a0]
r2, p2, k2 = signal.residue(num_haste_x_u, den_haste_x_u)
print('Resíduos, Polos e termo direto:')
print(r2, p2, k2)
# FT
Gs2 = co.tf(num_haste_x_u, den_haste_x_u)
print(Gs2)
p2, z2 = co.pzmap(Gs2, plot=True, grid=True, title='Pole Zero Map X/U')
print('Polos e zeros:')
print(p2, z2)
# Para X1 = THETA; X2 = THETA'; X3 = x; X4 = x'.
a21 = -((M + m)*m*g*l)/((m*l)**2 - (M + m)*(I + m*(l**2)))
a41 = -(g*(m*l)**2)/((M + m)*(I + m*(l**2))-(m*l)**2)
A = [[0,  1,  0,  0],
     [a21,  0,  0,  0],
     [0,  0,  0,  1],
     [a41,  0,  0,  0]]
b21 = (m*l)/((m*l)**2 - (M + m)*(I + m*(l**2)))
b41 = (I + m*(l**2))/((M + m)*(I + m*(l**2))-(m*l)**2)
B = [[0],
     [b21],
     [0],
     [b41]]
C = [[1, 0, 0, 0],
     [0, 0, 1, 0]]
D = [[0],
     [0]]
Gsee = co.ss(A, B, C, D)
# Não funcionou a conversão para TF com 2 saídas... ??? slycot error...
# No MatLab, tudo ok!!!
# GsTFs = co.ss2tf(Gsee)
print(Gsee)

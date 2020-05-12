import numpy as np
import matplotlib.pyplot as plt

#       1D Wave equation with Forward Time Central Space with artificial viscosity

L = 1
n = 201
h = L/(n-1)
sigma = 0.5
mu_2 = 0.25*(0.5*sigma*h**2)
bc = 1
ic = 0
n_iter = 10000
x = np.arange(0,L+h,h)
u = np.zeros(n)
u_new = np.zeros(n)
u = np.sin(10*x) + np.sin(40*x) + np.sin(160*x)
u[0] = u_new[0] = bc
plt.ion()
p, = plt.plot(x,u)

for j in range(n_iter):
        for i in range(1,n-1):
                u_new[i] = u[i] - 0.5*sigma*(u[i+1]-u[i-1]) + mu_2*(u[i+1]-2*u[i]+u[i-1])/h**2
        u_new[-1] = (1-sigma)*u[i] + sigma*u[i-1]
        u = u_new.copy()
        if j%10 == 0:
                p.set_ydata(u)
                plt.pause(0.5)
plt.pause(30)
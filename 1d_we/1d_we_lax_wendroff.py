import numpy as np
import matplotlib.pyplot as plt

#       1D Wave equation with Lax Wendroff Scheme

L = 1
n = 101
h = L/(n-1)
sigma = 0.1
bc = 1
ic = 0
n_iter = 1000
x = np.arange(0,L+h,h)
u = np.zeros(n)
u_new = np.zeros(n)
u = np.sin(10*x) + np.sin(50*x) + np.sin(250*x)
u[0] = u_new[0] = bc
plt.ion()
p, = plt.plot(x,u)

for j in range(n_iter):
        for i in range(1,n-1):
                up1 = 0.5*(u[i]+u[i-1])
                up2 = 0.5*(u[i]+u[i+1])
                upn1 = up1 - 0.5*sigma*(u[i]-u[i-1])
                upn2 = up2 - 0.5*sigma*(u[i+1]-u[i])
                up = 0.5*(upn1+upn2)
                u_new[i] = up - 0.5*sigma*(up2-up1)
        u_new[-1] = u_new[-2]
        u = u_new.copy()
        if j%10 == 0:
                p.set_ydata(u)
                plt.pause(0.1)
plt.pause(30)
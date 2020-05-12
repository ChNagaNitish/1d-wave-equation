import numpy as np
import matplotlib.pyplot as plt

#       1D Wave equation with Crank-Nicholson Scheme

L = 1
n = 101
h = L/(n-1)
sigma = 1.5
bc = 1
ic = 0
n_iter = 100
x = np.arange(0,L+h,h)
u = np.zeros(n)
#u = np.sin(10*x) + np.sin(50*x) + np.sin(250*x)
A = np.zeros((n-2,n-2))
for i in range(n-2):
        A[i,i] = 1
        if i!=0 and i!=n-3:
                A[i,i+1] = 0.5*sigma
                A[i,i-1] = -0.5*sigma
A[0,1] = 0.25*sigma
A[-1,-2] = -0.25*sigma
u[0] = bc

plt.ion()
p, = plt.plot(x,u)

def tdma(A_new,u):
        A = A_new.copy()
        B = np.zeros(n-2)
        u_new = np.zeros(n)
        u_new[0] = bc
        u_new[-1] = (1-sigma)*u[-1] + sigma*u[-2]
        B[1:-1] = u[2:-2] + 0.25*sigma*(u[1:-3]-u[3:-1])
        B[0] = u[1] + 0.25*sigma*(u[0]-u[2]) + 0.25*sigma*u_new[0]
        B[-1] = u[-2] + 0.25*sigma*(u[-3]-u[-1]) - 0.25*sigma*u_new[-1]
        for i in range(1,n-2):
                B[i] = B[i] - B[i-1]*A[i,i-1]/A[i-1,i-1]
                A[i,:] = A[i,:] - A[i-1,:]*A[i,i-1]/A[i-1,i-1]
        for i in range(n-4,-1,-1):
                B[i] = B[i] - B[i+1]*A[i,i+1]/A[i+1,i+1]
                A[i,:] = A[i,:] - A[i+1,:]*A[i,i+1]/A[i+1,i+1]
        for i in range(n-2):
                u_new[i+1] = B[i]/A[i,i]
        return u_new
for i in range(n_iter):
        u = tdma(A,u)
        if i%10 == 0 and i!=0:
                print(i)  
                p.set_ydata(u)
                plt.pause(1)
plt.pause(30)
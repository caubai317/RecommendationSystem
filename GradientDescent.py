from __future__ import division, print_function, unicode_literals
import math
import numpy as np 
import matplotlib.pyplot as plt

def grad(x):
    return -2*x + 2

def cost(x):
    return -x**2 + 2*x

def myGD1(eta, x0):
    x = [x0]
    for it in range(1000):
        x_new = x[-1] + eta*grad(x[-1])
        if abs(grad(x_new)) < 1e-3:
            break
        x.append(x_new)
    return (x, it)

print(myGD1(0.007,0.7))

a=np.array([[1,2,3,4],[5,6,7,8]])

print(a[:,0])
print(a[:,1])
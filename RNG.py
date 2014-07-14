# Paul Glenn
# MTH 437
# Book exercise
# Section 9.1 Problem 3
from numpy import *

def MCarea(myf,xi,xf,numpoints):
    '''Compute the area under the curve of f in the interval (a,b)
        using random numbers uniform on (0,1)
        and the specified number of points.'''
    a = 4; m = 9; b = 1
    x = empty(numpoints)
    u = empty(numpoints)
    x[0] = 1
    for i in range(numpoints-1):
        x[i+1] =(a*x[i]+b)%m
        u[i] = x[i+1]/m
    y = myf(u)
    return (xf-xi)*sum(y)/float(numpoints)
    
def f(x): return x**2.
A = MCarea

#Polynomial interpolation with monomial basis 
from numpy import *

def monoco(x,y):
    n = len(x)
    M = empty((n,n))
    M[:,0] = 1.
    for i in range(1,n):
        M[:,i] = x*M[:,i-1]
    return linalg.solve(M,y)

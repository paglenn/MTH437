# Use bisection method to solve the problem det(A) - 1000 == 0.

from numpy import array
from numpy.linalg import det

a = -100; b = 100; c = (a+b)/2.
eps = 10**-10
A = array([[1,2,3,c],[4,5,c,6],[7,c,8,9],[c,10,11,12]])

while abs(det(A) - 1000) >eps:
    c = (a+b)/2.
    for x in range(4):
        A[x][3-x] = c
    if det(A) == 1000: break
    elif det(A)<1000:
        a = c
    else:
        b = c
print c, det(A)

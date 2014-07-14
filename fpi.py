from math import *

#f = lambda x: (1+2*x**3)/(1+3*x**2)
f = lambda x: 0.5*(1+cos(2*x))
tol = 25 #max tries to ensure termination of program
x0 = 0.75 #Initial guess
numTries = 0

while numTries<tol:
    c= f(x0)
    x0 =c
    numTries += 1
    print 'Number of iterations:{:<10} Estimate: {:^10.9f}'.format(numTries,x0)

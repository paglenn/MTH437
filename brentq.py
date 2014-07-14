from math import *
from scipy.optimize import brentq

f = lambda x: tanh(x)

x0 , r =brentq(f,-1.1,1.09,xtol = 10**-15.,maxiter=6,full_output = True)
print x0, r 

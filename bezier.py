# Paul Glenn
# Homework 7 3.5X
# Calculate best reference points for 4-point bezier curve
#Based on maximum radial deviation.
from numpy import *

T = linspace(0.,1.,200)
V = linspace(0.551,0.553,2001)

# Radial deviation
e = lambda s: ((3.*s*t + (3.-6.*s)*(t**2.) + (3.*s-2)*(t**3.))**2. +\
    (1. +(3.*s-3.)*(t**2.) +(2.-3*s)*(t**3.))**2.)-1.

S = [] # to hold s-values
M = [] # to hold maximum radial deviations

for s in V:
    D = [] # to hold errors 
    for t in T:
        D.append(abs(e(s)))
    M.append(max(D))
    S.append(s)
    
c = 0
for j in range(len(M)):
    if M[j] == min(M):
        print 'Solution:' ,S[j]
        print 'Max deviation: ', M[j]
    else:
        c += 1
    
    

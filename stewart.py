#Stewart platform

from math import *
from bisection import bisect
from scipy.optimize import brentq

p1 = sqrt(5.)
p2 = p1 
p3 = p1 
L1 = 2.
L2 = sqrt(2.)
L3 = sqrt(2.)
gm = pi/2. #Gamma 
x1 = 4.
x2 = 0.
y2 = 4.

# th = theta 
a2 = lambda th: L3*cos(th)-x1
a3 = lambda th: L2*(cos(th)*cos(gm)-sin(th)*sin(gm))-x2
b2 = lambda th: L3*sin(th)
b3 = lambda th: L2*(sin(th)*sin(gm)+cos(th)*cos(gm))-y2

N1 = lambda th: b3(th)*(p2**2.-p1**2-a2(th)**2-b2(th)**2)-\
     b2(th)*(p3**2-p1**2-a3(th)**2-b3(th)**2)
N2 = lambda th: a2(th)*(p3**2.-p1**2-a3(th)**2-b3(th)**2)-\
     a3(th)*(p2**2-p1**2-a2(th)**2-b2(th)**2)
D  = lambda th: 2*(a2(th)*b3(th)-a3(th)*b2(th))

x = lambda th: N1(th)/D(th)
y = lambda th: N2(th)/D(th)

f = lambda w: N1(w)**2+N2(w)**2 - (D(w)*p1)**2


T = float(brentq(f,pi/4,pi/3))

print 'x = %g'%(x(T))
print 'y = %g'%(y(T))

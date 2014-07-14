# interp_runge.py
from numpy import *
from pylab import plot, show, xlabel, ylabel, title, subplot

from poly import newtonCoeffs,evalPoly

def runge(x):
	return 1.0/(1.0+25.0*x*x)

numnodes = input("Number of evenly spaced nodes: ")
x = linspace(-1.,1.,numnodes,endpoint=True)
y = runge(x)
c = newtonCoeffs(x,y)

xx = linspace(x[0],x[-1],2000)
poly = evalPoly(x,c,xx)
truerunge = runge(xx)

plot( x, y,         'bo')
plot( xx,poly     , 'm')
plot( xx,truerunge, 'k')
xlabel('x')
title('Polynomial interpolation (magenta) of runge (black)')
show()


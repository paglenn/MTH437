# interp_runge.py
from numpy import *
from pylab import plot, show, xlabel, ylabel, title, subplot

from poly import newtonCoeffs,evalPoly

def runge(x):
	return 1./(1.+12.*x*x)

numnodes = input("Number of Cheby nodes: ")
#x = linspace(-1.,1.,numnodes,endpoint=True)
i = array(range(numnodes))
theta = (2.*i+1)*pi/2./numnodes
x = cos(theta)

y = runge(x)
c = newtonCoeffs(x,y)

xx = linspace(x[0],x[-1],2000)
poly = evalPoly(x,c,xx)
truerunge = runge(xx)

plot( x, y,         'bo')
plot( xx,poly     , 'p')
plot( xx,truerunge, 'k')
xlabel('x')
title('Polynomial interpolation at Cheby nodes (magenta) of Runge (black)')
show()


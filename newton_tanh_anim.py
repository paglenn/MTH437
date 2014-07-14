# illustrate failure of newton's method applied to tanh

from numpy import *
from pylab import plot, ginput, show, clf, draw, xlim, ylim

def f(x):		return tanh(x)
def fprime(x): return 1.-tanh(x)**2

x = 0.5
xmin = -3.
xmax =  3.
xa=linspace(xmin,xmax,251)
plot( [xmin,xmax],[0.,0.], 'k' )
plot( xa, f(xa), 'b', linewidth=2.)
xlim( xmin, xmax )
ylim( -1.5,1.5 )
draw()
while( True ):
	point = ginput(1) 	# get new x0
	x = point[0][0]
	print x
	clf()
	plot( [xmin,xmax],[0.,0.], 'k' )
	plot( xa, f(xa), 'b', linewidth=2.)
	plot([x],[0.],'ko')
	nits = 2
	for i in range(nits):
		plot( [x,x],[0.,f(x)], 'k' )
		nextx = x - f(x)/fprime(x)
		xs = array([x-1.0*(nextx-x),nextx])
		plot( xs, f(x)+fprime(x)*(xs-x) ,'r' )
		plot([x],[f(x)],'bo')
		plot([nextx],[0.],'ro')
		x = nextx
	xlim( xmin, xmax )
	ylim( -1.5,1.5 )
	draw()
show()



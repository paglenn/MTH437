from numpy import *

def makeN( xdata ): # build the Newton matrix for the given nodes
	n = len(xdata)
	N = zeros((n,n))
	N[:,0] = 1.
	for j in range(1,n):
		N[j:,j] = N[j:,j-1] * ( xdata[j:] - xdata[j-1] )
	return N

def fs(a,b): # Forward substitution: 
             # solves a lower-triangular linear system ax=b.
             # Leaves a and b unchanged
	n = len(b)
	x = b.copy()
	for i in range(n):
		for j in range(i):
			x[i] -= a[i,j]*x[j]
		x[i] /= a[i,i]
	return x

def newtonCoeffs( xdata, ydata ): # compute the coeffs in the Newton basis
                                  # of the interpolating polynomial
	N = makeN( xdata )
	return fs( N, ydata )

def evalPoly(xdata,c,x): 
	# xdata are the nodes
	# c are the interpolating polynomial's coefficients in the Newton basis
	# x are the points where we want to evaluate the polynomial
	e = ones_like(x)
	p = zeros_like(x)
	n = len(xdata)
	for i in range(n):
		p += c[i]*e
		e *= (x-xdata[i])
	return p

'''
#Test it:

xdata = array([0.,2.,3.,2.5])
ydata = array([1.,2.,4.,-3.])

xarray = linspace(-0.5,3.5,300)
c = newtonCoeffs( xdata, ydata )
yarray = evalPoly(xdata,c,xarray)

from pylab import plot,show
plot(xarray,yarray)
plot(xdata,ydata,'ro')
show()
'''

















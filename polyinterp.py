from numpy import *

def makeN( x ):
    n = len(x)
    N = zeros((n,n))
    N[:,0]=1.
    for j in range(1,n):
        N[:,j]=N[:,j-1]*(x-x[j-1])
    return N

def evalpoly(xdata,c,x):
    e = ones_like(x)
    p = zeros_like(x)
    for i in range(len(xdata)):
        p += c[i]*e
        e *= (x-xdata[i])
    return p

x = array([0.,2.,3.,4])
y = array([1.,2.,4.,5])
N = makeN(x)
c = linalg.solve(N,y)
xarray = linspace(-1.,6.,300)
yarray = evalpoly(x,c,xarray)

from pylab import *
plot(xarray,yarray)
plot(x,y,'ro')
show()

from numpy import *
from scipy.special import erf
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

x = array([0.,0.5,1])
y = erf(x)
N = makeN(x)
c = linalg.solve(N,y)
xarray = linspace(0.,1.,300)
yarray = evalpoly(x,c,xarray)

from pylab import *
#plot(xarray,yarray)
plot(xarray,yarray-erf(xarray),'c')
#plot(x,y,'ro')
bound = abs(xarray*(xarray-0.5)*(xarray-1)*2/3/sqrt(pi))
plot(xarray,bound,'k')
plot(xarray,-bound,'k')
show()

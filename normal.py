# Find least squares solution to fit fit a model to a given set of data.
from numpy import *

m = 5000 #Number of points to take
##t = random.rand(m)
##y = pi + 4*t +0.2*(random.rand(m)-0.5) #Random noisy data with an obvious trend

#input data
t = array([1,3.,4,6])
y = array([2,2.,1,3])

from pylab import plot, show, axis
axis([0,7.,0,4.])
plot(t,y,'ro') #Red circles

#Use to find least squares solution
#Input x, then b
def fit(t,y):
    m = len(t)
    global r
    AT = vstack([ones(m),t]) #Create A transpose before A; easier
    A = AT.T
    ATA = dot(AT,A)
    ATb = dot(AT,y)
    x = linalg.solve(ATA,ATb)
    r = y - dot(A,x)
    RMSE = linalg.norm(r)/sqrt(len(r))
    print 'RMSE = ', RMSE
    return x

x = fit(t,y)
t0 = min(t)
t1 = max(t)
y0 = x[0] +x[1]* t0
y1 = x[0] + x[1]* t1
print 'alpha = ', x[0]
print 'beta = ', x[1]

# Add in RMSE
plot( [t0,t1], [y0,y1], 'b') #line in blue from entering points like this
show()

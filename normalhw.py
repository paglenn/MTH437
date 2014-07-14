# Find least squares solution to fit fit a model to a given set of data.

from numpy import *
from pylab import *

##m = 5000 #Number of points to take
##t = random.rand(m)
##y = pi + 4*t +0.2*(random.rand(m)-0.5) #Random noisy data with an obvious trend

#input data
x = array([1,3.,4,6]) 
y = array([2,2.,1,3])

axis([0,7.,0,4.])
plot(x,y,'ro') #plot initial data 
xlabel('x')
ylabel('y')
title('EX 9b least-squares fit')

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

m = fit(x,y)
x0 = min(x)
x1 = max(x)
y0 = m[0] +m[1]* x0
y1 = m[0] + m[1]* x1

print 'alpha = ', m[0]
print 'beta = ', m[1]

# Add in RMSE
plot( [x0,x1], [y0,y1], 'b') #linear model 
show()

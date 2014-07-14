from numpy import *
from pylab import *
from time import time

def MSRNG(N):
    r = empty(N)
    x = empty(N)
    m = 2.**31 - 1.
    a = 16807
    x[-1] = time()
    for i in range(N):
        x[i] = (a*x[i-1])%m
        r[i] = float(x[i])/m
    return r
        
    
N = int(raw_input('Number of points: '))
x = rand(N)
y = rand(N)

T1 = 4.*(2.*x-1.)**4+8*(2*y-1)**8. < 1. + 2*(2*y-1)**3 * (3*x-2)**2
T2 = (x-1.)**2 + y**2 > 0.25

TT = T1 & T2

print sum(TT)/float(len(TT))
r = MSRNG(N)
xi = r[0:N/2]
yi = r[N/2:N]

inx = x[where(TT)]
iny = y[where(TT)]
subplot(121,aspect = 'equal')
plot(xi,yi,'o')
subplot(122,aspect = 'equal') 
plot(inx,iny,'b.',alpha = 0.5)
show()

from numpy import *
from math import factorial
from pylab import plot, show, xlabel, ylabel
logx = linspace(-11.,-1.,4000)
x = 10.**logx
direct = sin(x)-x
ref = (-x**3.)/6+(x**5.)/factorial(5)-(x**7)/factorial(7)+(x**9)/factorial(9)
relerror=abs(1.*(direct-ref)/ref)
eps = 2.**-52
bound = (3.*eps)/x**2
plot(logx,log10(abs(relerror)),'b.')
plot(logx,log10(bound),'r')

xlabel('log(x)')
ylabel('log(relerror)')
show()



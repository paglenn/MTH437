from numpy import *
from pylab import *
logx = linspace(-16,-14,400)
x = 10**logx
D = (log(1+x))/x
ref = 1.-x/2.+(x**2.)/3.
relerror = (D-ref)/(1.*ref)
eps = 2.**-52.
bound = (1./2)*eps*(1./x)
plot(logx,relerror,'.')
plot(logx,bound)
plot(logx,-bound)
xlabel(r'$\log(x)$')
ylabel(r'relative error $\delta_{r}(x)$')
title(r'Relative error for direct evaluation of $\frac{\log(1+x)}{x}$')
savefig('errorplot.png')
show()

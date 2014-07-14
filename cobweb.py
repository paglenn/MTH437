# cobweb.py
from numpy import *
from pylab import plot,show,xlabel,ylabel,subplot, savefig

g = lambda x: 2.5*x*(1-x)  

lo = -3.
hi =  3
xa = linspace(lo,hi,2000)
gxa = g(xa)

subplot(111, aspect = 'equal') #111
lw = 1.
plot(xa,gxa,linewidth=lw)
plot(xa,xa,'k',linewidth=lw)
xlabel('x(i)')
ylabel('x(i+1)')

x = 0.3 #3/4

def up(x):
	plot( [x,  x], [  x ,g(x)],'r',linewidth=lw)

def across(x):
	plot( [x,g(x)],[g(x),g(x)],'g',linewidth=lw)

plot( [x,  x], [  lo,g(x)],'r',linewidth=lw) # up to g
for i in range(20):
	if i>0: up(x)
	across(x)
	x = g(x)

print x
show()


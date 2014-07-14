from numpy import *
from g7k15 import *

# adaptive algorithm using g7k15
# implemented recursively
def adaptive(f,a,b,tol):
	approx,errest,errestkmn = g7k15(f,a,b)
	if errestkmn < tol:
		return approx,errestkmn
	else:
		# split into two halves	
		midpt = (a+b)*0.5
		approxL, errestL = adaptive(f,a    ,midpt,tol*0.5)	
		approxR, errestR = adaptive(f,midpt,b    ,tol*0.5)	
		return approxL+approxR, errestL+errestR

# Test it!

from pylab import plot, show
count = 0
def testf4(x):
	global count
	plot(x,count*ones_like(x),'bo')
	count += 1
	return sin(x)

a = -3.
b = 3.
exact = F(b)-F(a)+0.01*(F(b)-F(a))
print 'Exact:        ', exact
tol=1.0e-13
approx = adaptive(blip,a,b,tol)
print 'Approximation:',approx
print 'Actual error:',approx[0]-exact
show()
quit()

































'''

def runge(x):
	return 1.0/(1.0+12.0*x*x)

def collage(x):
	shift = -1.7
	squeeze = 100.0
	return runge(x) + runge( squeeze*(x-shift) )

x = linspace(-3,3,1000)
f = collage(x)
from pylab import plot, show, figure
figure(1)
plot(x,f)
#show()
#quit()
figure(2)
count = 0
def testf5(x):
	global count
	plot(x,count*ones_like(x),'b.')
	count += 1
	return collage(x) #runge collage 
approx = adaptive(testf5,-3.0,3.0,1.0e-13)
print approx
show()

'''

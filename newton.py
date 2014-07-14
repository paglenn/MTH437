from math import tanh, cosh

def f_and_fprime(x):
	return tanh(x), (1./cosh(x))**2

#print f_and_fprime(2.)
#quit()

x=1.08
err = 10.**-15.

for i in range(10):
	print i,x
	f,fprime = f_and_fprime(x)
	step = -f/fprime
	x += step
	if abs(f) > err: print False
	else: print True

print x

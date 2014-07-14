
# Root finding with bisection method

from math import *

def sign(y):
	if y>0: return  1
	if y<0: return -1
	return 0

def bisection(f,a,b,tol):
	sfa = sign(f(a))		# so we won't have to call f or sign multiple times at a or b
	sfb = sign(f(b))
	if sfa == 0: return a	# a is a root
	if sfb == 0: return b	# b is a root
	if sfa == sfb:
		print "You didn't give me a bracket!"
		quit()
	while abs(a-b) > tol:
		print a,b			# just to see how things are proceeding
		c = (a+b)/2.		# midpoint
		sfc = sign(f(c))
		if sfc == 0: return c	# hit a root exactly, by good luck
		if sfc == sfa:		
			a = c
		else:
			b = c
	return (a+b)/2.
		
def myf(x):
	return cos(x) - 2*x

# Example of use:
# r = bisection(myf,0,10,1.0e-13)
# print "Root ~", r

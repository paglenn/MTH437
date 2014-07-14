# Paul Glenn
# HW 8 15.1
# Modification of Minimize-golden-hw3.py
# 'Idea 3'

from math import sqrt

def f(x): return (x-1./3.)**2

golden = (-1.+sqrt(5.))/2.
print golden

a = -500.  ; fa = f(a)
c = 1000.  ; fc = f(c)
b = a + (   golden)*(c-a)
w0 = abs(c-a)
w = w0
tol = 1.e-7
i = 0
print a,b,c
while(w>tol):

	if abs(b-a)>abs(c-b):					
		d = a + (b-a)/2.			
	else:						
		d = a + (c-b)/2.	 

	if d < b:
		if f(d) >= f(b):
			a,b,c = d,b,c
		else:
			a,b,c = a,d,b
	else:
		if f(d) >= f(b):
			a,b,c = a,b,d
		else:
			a,b,c = b,d,c
	w = abs(c-a)
	print "Bracket: (",a,b,c,"), width =",w
	i += 1

print "Approximate root:",b
print "Average bracket shrinkage per iteration",(w/w0)**(1./float(i))



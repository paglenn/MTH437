# Python translation of Sauer code by JR
# Program 3.5 Calculation of spline coefficients
# Calculates coefficients of cubic spline
# Input: x,y vectors of data points
#   plus two optional extra data v1, vn
# Output: matrix of coefficients b1,c1,d1b2,c2,d2...
from numpy import *
def splinecoeff(x,y):
	n=len(x); v1=0; vn=0
	A=zeros((n,n))            # matrix A is nxn
	r=zeros(n)
	dx = empty(n-1);	dy = empty(n-1)
	for i in range(n-1):              # define the deltas
		 dx[i] = x[i+1]-x[i]; dy[i]=y[i+1]-y[i]
	for i in range(1,n-1):              # load the A matrix
		 A[i,i-1:i+2] = hstack( [dx[i-1], 2*(dx[i-1]+dx[i]), dx[i]] )
		 r[i]=3*(dy[i]/dx[i] - dy[i-1]/dx[i-1]) # right-hand side
	# Set endpoint conditions
	# Use only one of following 5 pairs:
	A[0,0] = 1              # natural spline conditions
	A[n-1,n-1] = 1
	# Other options cut out for now
	coeff=zeros((n,3))
	coeff[:,1]= linalg.solve(A,r)  	# solve for c coefficients
	for i in range(n-1):              # solve for b and d
		 coeff[i,2]=(coeff[i+1,1]-coeff[i,1])/(3*dx[i])
		 coeff[i,0]=dy[i]/dx[i]-dx[i]*(2*coeff[i,1]+coeff[i+1,1])/3
	coeff=coeff[0:n-1,:]
	return coeff

# Program 3.6 Cubic spline plot
# Plots spline from data points
# Input: x,y vectors of data points
# Output: none
def splineplot(x,y):
	n=len(x)
	coeff=splinecoeff(x,y)
           # clear figure window and turn hold on
	for i in range(n-1):
		x0=linspace(x[i],x[i+1],100)
		dx=x0-x[i]
		y0=coeff[i,2]*dx   # evaluate using nested multiplication
		y0=(y0+coeff[i,1])*dx
		y0=(y0+coeff[i,0])*dx+y[i]
#		plot([x[i],x[i+1]],[y[i],y[i+1]],'bo')
		plot(x0,y0)

from pylab import plot, show, figure, savefig, title
x = [0.,1.,2.]
y = [0.,1.,6.]
# figure(figsize=[19,3])
plot(x,y,'mo')
splineplot( x,y )
title('Ex 8b spline')
savefig('ex8b1.png')
show()




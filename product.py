from numpy import *
from pylab import plot,show,legend
# Chebychev nodes
numnodes = 5
i = array(range(numnodes))
theta = (2.*i+1)*pi/2./numnodes
xcheby = cos(theta)

entries = [ \
[ [0.,0.52,-0.52,0.76,-0.76],  'John'  ], \
[ [0.,0.33,-0.33,0.66,-0.66],  'Arjun' ], \
[ [0.,1.,-1.,-0.5,0.5],        '#1'    ], \
[ [0.,0.875,-0.875,-0.75,0.75],'#2'    ], \
[ [0.,1.,-1.,-0.75,0.75],      'Saeed' ], \
[ [0.,0.1587,0.8413,-0.1587,-0.8413], '#Jim'], \
[ [0.,-0.9,0.9,-0.5,0.5],      '#3'    ], \
[ xcheby,                      'Cheby' ] ]
print entries

xa = linspace(-1.,1.,2000) # a dense set of evaluation points

for entry in entries:
	x = entry[0]
	prod = ones_like(xa)
	for xi in x:
		prod *= (xa-xi)
	print entry[0], max(abs(prod))
	theColor = random.rand(3)
	plot(xa,prod,color=theColor,linewidth=2)
	
theLegend = [entry[1] for entry in entries]
print theLegend
legend( theLegend )
plot([-1.,1.],[0.,0.],'k')

show()


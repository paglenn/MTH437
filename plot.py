from numpy import *
from pylab import plot,axes,show
from project import *

data = loadtxt('Convergence.dat')
plot(data[:,1],data[:,2],'b-')
plot(data[:,5],data[:,6],'mo')
axes().set_aspect('equal','datalim')
show()

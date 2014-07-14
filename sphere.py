# Random Hemisphere.py
# Author: Paul Glenn
# MTH 437 HW 8 15.1 X2
# 11/16/2012
# Generates random points uniformly on the unit hemisphere.

from numpy import *
from pylab import *
from time import time
import mpl_toolkits.mplot3d.axes3d as p3

numpoints = 200
theta = 2*pi*rand(numpoints) #theta in this case corresponds to the polar angle
phi = arccos(rand(numpoints)) # and Phi is the co-latitude.
x = outer(sin(phi),cos(theta))
y = outer(sin(phi),sin(theta))
z = outer(cos(phi),ones(size(theta)))
fig = figure()
ax = p3.Axes3D(fig)
ax.scatter(x,y,z)
ax.set_title('Uniform on the unit sphere')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
savefig('sphere.png')
show()




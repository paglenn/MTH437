from numpy import *

V = array([1,2,3,4])
U = array([1,1,2,3])

H = hstack([U,V])
Vp= vstack([U,V])

print "Hstack: "
print H
print "Vstack: "
print Vp

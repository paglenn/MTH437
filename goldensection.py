# Paul Glenn
# Homework 8 15.1 X2
# Bezier circle approximation to a circle
from math import sqrt
from numpy import *

# Bezier cubic formula 
def f(s,*args):
    global TrueRadius
    x1 = -1; y1 = 0.
    x2 = -1.; y2 = s
    x3 = 1.; y3 = s
    x4 = 1.; y4 = 0.
    bx = 3*(x2-x1)
    by = 3*(y2- y1)
    cx = 3*(x3-x2) - bx
    cy = 3*(y3-y2) - by
    dx = x4 - x1 - bx - cx
    dy = y4 - y1 - by -cy
    t = linspace(0.,1.,100)
    x = x1 + (bx)*t + (cx)*t**2. + (dx)*t**3.
    y = y1 + (by)*t + (cy)*t**2. + (dy)*t**3.
    if 1 in args:
        return x,y
    else:
        r = sqrt(x**2. + y**2.)
        r_e = abs(TrueRadius-r) # Error vector 
        return max(r_e)

TrueRadius = 1.
golden = (-1.+sqrt(5))/2. # Golden ratio

a = 0.
c = 2.
b =  a + ( golden)*(c-a) # interval choice 
w0 = abs(c-a)
w = w0
tol = 1.e-7
i = 0

while(w>tol):
    if abs(b-a)>abs(c-b):
        d = a + (1.-golden)*(c-a)
    else:
        d = a + (golden)*(c-a)

    if d < b:
        if f(d) >= f(b): a,b,c = d,b,c
        else: a,b,c = a,d,b
    else:
        if f(d) >= f(b): a,b,c = a,b,d
        else: a,b,c = b,d,c
    w = abs(c-a)
    #print 'Bracket: (',a,b,c,'), width = ', w
    i += 1

print """Approximate root: %s
Average bracket shrinkage per iteration = %s
Maximum radial deviation: %s"""%(b,(w/w0)**(1./float(i)),f(b))

# Now to plot the resulting circle...
from pylab import plot, show, title, savefig
x,y = f(b,1)
plot(x,y)
#and the true unit circle 
theta = linspace(0,pi,100)
xt = cos(theta)
yt = sin(theta)
plot(xt,yt,'k')
title('Bezier semicircle (true circle in black)')
savefig('Bezier.png')
show()


from numpy import *

eps = 10.**-10
f = lambda u,v: u**2.-4*(v**2.)-4.
g = lambda u,v: (u-1)**2.+(v**2.)-4.

X = array([1.,1])
u,v = [1,1]
F = lambda x,y: array([f(x,y),g(x,y)])
f1,f2 = F(u,v)

while abs(f1) >= eps or abs(f2) >=eps:
    DF = array([[2*u,-8*v],[2*(u-1),2*v]])
    S = linalg.solve(DF,-F(u,v))
    u += S[0]
    v += S[1]
    f1,f2 = F(u,v)
        
print " u = %s \n v = %s"%(repr(u),repr(v))

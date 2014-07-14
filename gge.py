from numpy import *
from cdiff import cdjac

def newton(thefunc, x , tol):
    n = x.shape[0]
    while(True):
        f = thefunc(x)
        df = cdjac( thefunc, x)
        s = linalg.solve(df,-f)
        x += s
        if F(x)[0]< tol and F(x)[1]<tol:
            return x
            break
##        
##f1 =     
##g = lambda u: (u[0]-1)**2.+u[1]**2.-4.
##f = lambda u: (u[0]**2.)-4*(u[1]**2.)-4
##F = lambda u: array([f(u),g(u)])
##x = array([1.,1.])
##eps = 10**-10.
##X = newton(F,x,eps)

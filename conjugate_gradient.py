from numpy import *
from scipy.optimize import bracket, brent
from source_code import *

Re = getEarthRadius()
c = getSpeedOfLight()/Re
def cg(M,x):
    M[:,0:3] /= Re
    '''Input Matrix and initial guess vector'''
    def f(xi,*args):
        x = copy(xi)
        r = zeros(size(M,0)) 
        G = zeros(4)
        for i in range(size(M,0)):
            g = zeros(4)
            r[i] = ((x[0]-M[i,0])**2. +(x[1]-M[i,1])**2. + (x[2]-M[i,2])**2.)**(0.5) 
            g[0] = (x[0]-M[i,0])/r[i]
            g[1] = (x[1]-M[i,1])/r[i]
            g[2] = (x[2]-M[i,2])/r[i]
            g[3] = c
            r[i] -= c*(M[i,3]-x[3]) #then add in last part -c(t-d)
            G += (2*r[i])*g #gradient vector 
        r_squared = (linalg.norm(r))**2
        if 1 in args:
            return G  #Gradient vector 
        else:
            return r_squared  #residual value

    def fline(alpha,f,x,d): # For brent: step in minus gradient direction
        return f(x+alpha*d)

    d = -f(x,1)
    r = d
    tol = 10**-9.

    #CG loop                  
    while(abs(f(x))>tol):
        alpha = brent(fline,args=(f,x,d))
        xn = x + alpha*d
        rn = -f(xn,1)
        x = xn
        beta = dot(rn,rn)/dot(r,r)
        d = rn + beta*d
        r = rn
    return x
    
    

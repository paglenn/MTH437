## Mini-project program
## Paul Glenn
## Due Oct 19,2012

from numpy import *
from pylab import *

# Functions
def cdjac(f,x): # returns a derivative matrix df created in 
                # the calling routine 
    eps = finfo( type(x[0]) ).eps # machine epsilon from numpy 
    delta = eps**(1.0/3.0)*linalg.norm(x,inf); 
    xplus = x.copy() 
    xminus = x.copy() 
    n = x.shape[0] 
    df = empty((n,n))
    for i in range(n): 
        xplus[i] += delta;  # perturb one component 
        xminus[i] -= delta; 
        fplus  = f(xplus); 
        fminus = f(xminus); 
        df[:,i] = (fplus-fminus)/(2*delta); 
        xplus[i] = x[i]     # reset perturbed component 
        xminus[i]= x[i] 
    return df

def newton(thefunc, x , tol):
    n = x.shape[0]
    #print n
    while(True):
        f = thefunc(x)
        df = cdjac(thefunc, x)
        s = linalg.solve(df,-f)
        x += s
        if linalg.norm(s)<tol:
            return x

# 16 Equations
def F(v):
    global g, m, L, n, PL, PR
    x = hstack([PL[0],v[0:n],PR[0]]) 
    y = hstack([PL[1],v[n:2*n],PR[1]])
    t = v[2*n:3*n+1]
    f = empty(3*n+1)
    for i in range(n):
        f[i] = L[i+1]*t[i]*(x[i] - x[i+1]) + L[i]*t[i+1]*(x[i+2] - x[i+1])
    for i in range(n):
        f[i+n] = L[i+1]*t[i]*(y[i]-y[i+1]) + L[i]*t[i+1]*(y[i+2]-y[i+1])\
                 -L[i]*L[i+1]*m[i]*g
    for i in range(n+1):
        dist = array([x[i+1]-x[i],y[i+1]-y[i]])
        f[i+2*n] = L[i]**2.-(linalg.norm(dist))**2.
    return f

p = 10**(-4.)
# Initial Data 
g = 981 #cgs units: L in cm, 
n = 5
eps = 10**-9 # Tolerance;  
m = array([225,98.20,58.10,96.05,81.98])
L = array([79.7,52.5,26.5,60.9,30.1,111.2])
PL = [0.0,0.0]
PR = [copy(L[-1])+p,-sum(L[:-1])]
PZ = copy(PR)
PF = array([312.0,11.9])

# Initial guess: (Almost) Vertical configuration
X = rand(5)*0.01
Y = array([-sum(L[:i+1]) for i in range(5)])
T = array([g*sum(m[i:]) for i in range(5)]+[0.])
v = hstack([X,Y,T])  #v is in form theXs, theYs, theT(ension)s


# Homotopy 
for h in linspace(0.,1.,50):#range(1,101,1):
    PR =(1-h)*PZ+h*PF
    newton(F,v,eps)
    x = hstack([PL[0],v[0:n],PR[0]])
    y = hstack([PL[1],v[n:2*n],PR[1]])
    
#Plotting
plot(x,y)
plot(v[0:n],v[n:2*n],'ro') #Mass coordinates are in red 
xlabel('x')
ylabel('y')
title('Mini-project')
savefig('solution')
print 'Solution: '
print v
show()

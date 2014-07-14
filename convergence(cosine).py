## Prerna Gera
## Paul Glenn
## Zhao Wu
## MTH 437/537

from numpy import *
from project import *
from scipy.optimize import bracket, brent

##########################Conjugate Gradient Code ##########################
def cg(M,x):
    Re = getEarthRadius()
    c = getSpeedOfLight()/Re
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
    while(abs(f(x,2))>tol):
        alpha = brent(fline,args=(f,x,d))
        xn = x + alpha*d
        rn = -f(xn,1)
        x = xn
        beta = dot(rn,rn)/dot(r,r)
        d = rn + beta*d
        r = rn
    return x
    
#########                   GetUsTogether               #####################
def GetUsTogether(): 
    c = getSpeedOfLight()
    R = getEarthRadius() 
    x_guess = array([0.,0,1,0]) 
    D = linalg.norm
    xi = R*cg(getGPS1Data(),x_guess)[:3]
    ref= R*cg(getGPS2Data(),x_guess)[:3]
    x0 = ref- xi
    walkPerson1(25)
    xc = R*cg(getGPS1Data(),x_guess)[:3]
    x1 = xc -xi
    dps = D(x1)/25
    print dps
    i = 1
    tol = 9.
    xv = x0 - x1
    #theta = arccos((D(xv)**2+D(x1)**2-D(x0)**2)/(2.*D(xv)*D(x1)))
    theta1 = math.atan2(xc[1]-xi[1],xc[0]-xi[1])
    theta2 = math.atan2(xc[1]-ref[1],xc[0] -ref[0])
    theta = theta2-theta1
    turnPerson1(theta)
    print theta,theta1,theta2
    error =D(xv)
    xcg = xc
    j=0
    L = []
    steps = 150

    while(error > tol/2.):
        L.append(error)
        walkPerson1(steps)
        if j%5 == 0:
            xc = R*cg(getGPS1Data(),hstack((xc/R,0.1)))[:3]
            error = D(xc-ref)
        if error > L[j]: turnPerson1(theta/2);
        elif abs(error - L[j]) < tol: turnPerson1(-theta/2);
        if error < 500: steps = 50
        if error < 200: steps = 15
        if error < 50: steps = 5
        #print error
        j+=1
        if j%20 ==0:
            print 'You are ',error,' meters away.'
    print error    
##    while(error > tol):
##        L.append(error)
##        xc = R*cg(getGPS1Data(),hstack((xc/R,0.1)))[:3]
##        error = D(xc-ref)
##        walkPerson1(15)
##        print error
##        j+=1
begin('Convergence')
GetUsTogether()

## Prerna Gera
## Paul Glenn
## Zhao Wu
## MTH 437/537 Final Project:
##Team: Convergence

from numpy import *
from project import *
from scipy.optimize import bracket, brentq

##############  Conjugate Gradient: 'Where am I?'                 #############
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

    def fline(alpha,f,x,d): # For brentq: step in minus gradient direction
        return f(x+alpha*d)

    d = -f(x,1)
    r = d
    tol = 10**-9.

    #CG loop
    while(abs(f(x))>tol):
        alpha = brentq(fline,args=(f,x,d))
        xn = x + alpha*d
        rn = -f(xn,1)
        x = xn
        beta = dot(rn,rn)/dot(r,r)
        d = rn + beta*d
        r = rn
    return x

######          Get Us Together! (Apply Heisenberg Compensator?)       #########

def GetUsTogether():
    R = getEarthRadius();
    x_guess = array([0.,0,1,0]) #rescaled guess; c= Re=1
    D = linalg.norm
    xi = R*cg(getGPS1Data(),x_guess)[:3]
    ref= R*cg(getGPS2Data(),x_guess)[:3]
    x0 = ref- xi
    walkPerson1(25)
    xc = R*cg(getGPS1Data(),x_guess)[:3]
    x1 = xc -xi
    dps = D(x1)/25
    xv = x0 - x1
    theta1 = math.atan2(xc[1]-xi[1],xc[0]-xi[0])
    theta2 = math.atan2(ref[1]-xc[1],ref[0] -xc[0])
    theta = theta1-theta2
    prev=theta2
    turnPerson1(theta)
    print theta,theta1,theta2
    error =D(xv)
    j=0
    L = []
    while(True):
        L.append(error)
        error = D(xc-ref)
        walkPerson1(75)
        xi = xc.copy()
        xc = R*cg(getGPS1Data(),hstack((xc/R,0.1)))[:3]
        theta1 = math.atan2(xc[1]-xi[1],xc[0]-xi[0])
        theta2 = math.atan2(ref[1]-xc[1],ref[0] -xc[0])
        theta = theta1-theta2
        turnPerson1(theta)
        walkPerson1(35)
        if error<100:walkPerson1(20)
        if error<50:walkPerson1(15)
        if error<20:walkPerson1(10)
        j+=1
noiseOn()
begin('keylimepie')
GetUsTogether()

from numpy import *

def GN(res,x): #Residual minimization for nonlinear least squares problems 
    eps = finfo(float).eps #machine epsilon from numpy
    for i in range(10):
        DR = cdjac(res,x)
        DRT = DR.T
        DFTDF = dot(DRT,DR)
        s = linalg.solve(DRTDR,-DR)
        x += s
       
def cdjac(f,x): # returns a derivative matrix df created in 
                # the calling routine 
    eps = finfo( type(x[0]) ).eps # machine epsilon from numpy 
    delta = eps**(1.0/3.0)*linalg.norm(x,inf); 
    xplus = x.copy() 
    xminus= x.copy() 
    n = x.shape[0]
    df = empty((n,n))
    for i in range(n): 
        xplus[i] += delta;  # perturb one component 
        xminus[i]-= delta; 
        fplus  = f(xplus); 
        fminus = f(xminus); 
        df[:,i] = (fplus-fminus)/(2*delta); 
        xplus[i] = x[i]     # reset perturbed component 
        xminus[i]= x[i] 
    return df

res = lambda x: array([\
	sqrt((x[0]+1)**2.+x[1]**2.)-1,\
	sqrt((x[0]-1)**2.+(x[1]-0.5)**2.)-0.5,\
	sqrt((x[0]-1)**2.+(x[1]+0.5)**2.)-0.5])
x = array([0,0.])
GN(res,x)

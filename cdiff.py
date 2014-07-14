from numpy import *

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

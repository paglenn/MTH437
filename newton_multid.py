from numpy import *

def newton(f_and_df, x, abstol ):
    while True:
        f, df = f_and_df(x)
        s = linalg.solve( df, -f)
        x += s
        print x
        if linalg.norm(s) < abstol:
            return x
        
def myfanddf(x):
    u,  v = x
    f = array( [v-u**3, u*u+v*v - 1.])
    df = array( [[-3.*u*u, 1.], [2.*u,2.*v]] )
    return f, df

x = array( [1., 2.] ); print x
mytol = 1.e-10
r = newton( myfanddf,x, mytol)
print r
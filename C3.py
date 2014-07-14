from numpy import *

for n in [100,200,300,400,500]:
    A = empty([n,n])
    x = array([1 for j in range(n)])
    for i in range(n):
        for j in range(n):
            A[i,j] = abs(i - j) + 1
    b = dot(A,x)
    xc = linalg.solve(A,b)
    nfe = linalg.norm(x-xc,inf)
    nbe = linalg.norm(b-dot(A,xc),inf)
    nx = float(linalg.norm(x,inf)); nb = linalg.norm(b,inf)
    print 'n = ', n
    print '||FE|| = ', nfe
    print 'emf = ', (nfe/nx)/(nbe/nb)
    print 'cond A = ', linalg.cond(A)
    print '\n'

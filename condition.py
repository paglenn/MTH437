from numpy import *

n = 6

A = random.rand(n,n)

A[1,0]=7.77777777

x=ones(n)

b=dot(A,x)

xc = linalg.solve(A,b)

fe = xc -  x

print A

print 'cond A = ', linalg.cond(A,inf)

print 'norm A = ', linalg.norm(A,inf)

print 'x = ', x

print 'Ax=',b

print 'xc = ',xc

print 'forward error = ', fe

print 'relative fe = ', \
    linalg.norm(fe,inf)/linalg.norm(x,inf)
    

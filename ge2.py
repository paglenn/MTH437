# LU factorization attempt
from numpy import *

A = array([[2,1,-4],[1,-1,0.965],[-1,3,-2]]) #Coefficient matrix
B = array([-7,-2,6.])
print linalg.solve(A,B)
n = len(B)
L = identity(n) # Basis for lower triangular L
# Elimination
for j in range(n-1):
    for i in range(j+1,n):
        mu = -A[i,j]/A[j,j]
        L[i,j]=-mu
        for k in range(j+1,n):
            A[i,k]+=mu*A[j,k]
        B[i]+=mu*B[j]
        A[i,j]=0
    U = A #Upper triangular Echelon matrix
print 
# Back-substitution
for j in range(n-1,-1,-1):
    for i in range(0,j):
        c = A[i,j]/A[j,j]
        B[i] -= c*B[j]
    B[j]/=A[j,j]

print 'x = ',B
print 'LU = '
print  mat(L)*mat(U)        

from numpy import *

M = [[-10.,6],[-100.,52],[-600.,301],[-599,301]]
x = array([1.,1])
b = array([3,6.01])
A = array([[1,2],[2,4.01]])
nx = linalg.norm(x,inf)
nb = linalg.norm(b,inf)
print 'cond A = ', linalg.cond(A,inf)
print '{:<10}{:<10}{:<10}{:<15}{:<10}{:<10}{:<10}{:>15}'\
      .format('Xc','FE','||FE||','rel ||FE||','BE','||BE||','rel ||BE||','emf')
for xc in M:
    fv = xc-x # Forward error 
    bv = b-dot(A,xc) #Backward Error                                         
    fe = linalg.norm(fv,inf)
    be = linalg.norm(bv,inf)
    rfe = fe/nx
    rbe = be/nb
    emf = rfe/rbe
    print '{:<10}{:<10}{:<10}{:<15}{:<10}{:<10}{:<10}{:>15}'\
      .format('[%g,'%(xc[0]),'[%g,'%(fv[0]),fe,rfe,'[%g,'%(bv[0]),be,'%.4f'%(rbe),'%i'%(emf))
    print '{:<10}{:<10}{:<10}{:<15}{:<10}{:<10}{:<10}{:>15}'\
      .format('%g]'%(xc[1]),'%g]'%(fv[1]),'','','%g]'%(bv[1]),'','','')
    

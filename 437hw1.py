#                          MTH 437 HW 1
# 0.0 X0
# Author: Paul Glenn
from math import cos

x = 2.0 #Initial guess
eps = 1.1*10**-16 #Just allows it to terminate with near-perfect agreement
g = open('HW1.txt','w+')
while abs(cos(x)-x)>eps:
    x = cos(x)
    g.write('guess = {:<20} | cos(x) = {:^10}'.format(repr(x),repr(cos(x)))+'\n')
    #repr so no digits left behind; also meets criteria for string output
g.close()

# Lecture on slicing Numpy arrays

from numpy import *
##set_printoptions(precision=8)
##a = random.rand(5,4)
##b = random.rand(5,1)
##print a
##print a[0:3,-1] # Print elements 1-3 of last column
##print a[:,0] # Print all rows, first column
##print a[:,0].reshape((b.shape)) #numpy takes a tuple 
##print a.shape[0] # Number of rows; 1 for number of columns

a = ones((3,2))
print a
##b = a.reshape(6)
##print a
##print b
##b[3] = 77.
##print a #changing b changes a; b is really just a reference
##print b

b = a.copy().reshape(6) #Creates entirely new copy instead of ref to a 
b[3]= 77.
print a
print b

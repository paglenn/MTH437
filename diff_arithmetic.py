# Paul Glenn
# MTH 437 Numerical Analysis
# Homework 9 
# Differentiation arithmetic/ Automatic Differentiation
import math
class valnder:

    def __init__(self, val = 0.0, der = 0.0 ): #Constructor
        self.val = val
        self.der = der

    def __add__( self, g): #Addition
        return valnder( self.val + g.val, self.der + g.der)

    def subtract(self,g): #Subtraction
        return valnder( self.val-g.val,self.der-g.der)

    ### 5.1 X2 (a)
    def mult(self,g): #Multiplication
        return valnder(self.val*g.val,self.val*g.der+self.der+g.val)

    def div(self,g): #Division
        try: assert g.val != 0 #Division by zero is obviously not allowed
        except AssertionError: return valnder('Undefined','Undefined')
        return valnder(self.val/g.val,
                       (g.val*self.der-self.val*g.der)/(g.val*g.val))

    def show(self ): #Printing class instances
        print "(",self.val, ",", self.der, ")"

    def sin(self): #sine function
        return valnder (math.sin(self.val),math.cos(self.val)*self.der)
    
    ### 5.1 X2 (b)
    def cos(self): #cosine function
        return valnder(math.cos(self.val),-math.sin(self.val)*self.der)
    
    def absval(self): #Absolute value
        if self.val == 0: return valnder(0.,'DNE') #
        else: #x/abs(x) returns 1 if x>0 and -1 if x<0; extracts sign
            x = math.sqrt(self.val*self.val)
            return valnder(x,self.val/abs(self.val)*self.der)

    def log(self): #Natural Logarithm   
        try: assert self.val >0 # Logarithm only defined over positive reals 
        except AssertionError: return valnder('Undefined','Undefined')
        return valnder(math.log(self.val),self.der/self.val)
### End class declaration
    
f = valnder(24./7,3.) # f(x)= 3x at x=8/7 
g = valnder(8./7,1.) #g(x) = x at x = 8/7
h = f.cos().div(g).absval().log()
print 'Automatic Differentiation gives: '; h.show()

##Actual formula for comparison
TrueVal = math.log(abs(math.cos(24./7)/(8./7)))
TrueDer = -(3*math.tan(24./7)+7./8)
print 'True Value and Derivative: ';print (TrueVal,TrueDer)


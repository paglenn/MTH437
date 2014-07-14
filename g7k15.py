from numpy import *

# Data generated using these Mathematica commands, 11/28/2012:
# n = 7; precision = 20;
# {absc, weights, errweights} = 
# NIntegrate`GaussKronrodRuleData[n, precision]
# {absc*2 - 1, weights*2}

k15nodes = array([
-0.9914553711208126392, 
-0.9491079123427585245, 
-0.8648644233597690728, 
-0.7415311855993944399, 
-0.5860872354676911303, 
-0.4058451513773971669, 
-0.2077849550078984676, 
 0., 
 0.2077849550078984676, 
 0.4058451513773971669, 
 0.5860872354676911303,  
 0.7415311855993944399, 
 0.8648644233597690728, 
 0.9491079123427585245, 
 0.9914553711208126392])

k15weights = array([
0.022935322010529224964, 
0.06309209262997855329, 
0.10479001032225018384, 
0.14065325971552591875, 
0.16900472663926790283, 
0.1903505780647854099, 
0.20443294007529889241, 
0.2094821410847278280, 
0.20443294007529889241, 
0.1903505780647854099, 
0.16900472663926790283, 
0.14065325971552591875, 
0.10479001032225018384, 
0.06309209262997855329, 
0.022935322010529224964]) 

# data from Wikipedia :-} 11/16/11
g7weights = array( [
0.129484966168870,
0.279705391489277,
0.381830050505119,
0.417959183673469,
0.381830050505119,
0.279705391489277,
0.129484966168870
])

def g7k15(f,a,b):  # Gauss-Kronrod 7-15 quadrature
	global k15nodes,k15weights,g7weights
	halfwidth = (b-a)/2.0 
	nodes = (a+b)*0.5 + k15nodes*halfwidth  # shift and scale nodes from [-1,1] to [a,b]
	f15vals = f(nodes)
	integralEstimateK15 = dot(k15weights,f15vals)*halfwidth

	f7vals = f15vals[1::2] # re-use the K15 function evaluations for G7
	integralEstimateG7  = dot( g7weights,f7vals)*halfwidth
	
	errorEstimate    = abs( integralEstimateK15 - integralEstimateG7 ) # super-conservative
	errorEstimateKMN = (200.*errorEstimate)**1.5  # Kahaner, Moler, Nash, p154

	return integralEstimateK15, errorEstimate, errorEstimateKMN

print "\nTest 1: constant function"
def testf1(x):
	return 0.*x + 1.
q = g7k15(testf1,2,7)
print q
exact = 5.0
print "Actual error:", q[0]-exact

print "\nTest 2: low degree polynomial"
def testf2(x):
	return x*x
q = g7k15(testf2,1,2.0)
print q
exact = 2.0**3/3. - 1.0**3/3.
print "Actual error:", q[0]-exact

print "\nTest 3: exponential function"
def testf3(x):
	return exp(2*x)
a = -2.; b = 1.
q = g7k15(testf3,a,b)
print q
exact = exp(2.*b)/2.0 - exp(2.*a)/2.0
print "Actual error:", q[0]-exact

print "\nTest 4: Runge function"
def runge(x):
	return 1./(1.+12.*x*x)
a = -3.; b = 3.
q = g7k15(runge,a,b)
print q
def F(x):
	return arctan(2.*sqrt(3.0)*x)/2./sqrt(3.)
print
exact = F(b)-F(a)
print "Exact",exact
print "Actual error:", q[0]-exact


print "\nTest 5: Runge function with a blip"
shift = -2.1
squeeze = 100.#100.
from pylab import plot, show, subplot, xlabel, ylabel
count = 0
def blip(x):
	global count
	plot(x,count*ones_like(x),'b.')
	count += 1
	return runge(x) + runge( squeeze*(x-shift) )

a = -3.; b = 3.
subplot(211); xx = linspace(a,b,3000); plot( xx, blip(xx) ); 
count = 0
q = g7k15(blip,a,b)
print q
exact =  F(b)-F(a)
exact += (F(squeeze*(b-shift))-F(squeeze*(a-shift)))/squeeze
print "exact",exact
print "Actual error:", q[0]-exact

print "\nTest 6: Runge function with a blip using adaptive algorithm"
# adaptive algorithm using g7k15
# implemented recursively
def adaptive(f,a,b,tol):
	approx,errest,errestkmn = g7k15(f,a,b)
	if errestkmn < tol:
		return approx,errestkmn
	else:
		# split into two halves	
		midpt = (a+b)*0.5
		approxL, errestL = adaptive(f,a    ,midpt,tol*0.5)	
		approxR, errestR = adaptive(f,midpt,b    ,tol*0.5)	
		return approxL+approxR, errestL+errestR
subplot(212) 		
q = adaptive(blip,a,b,1.0e-8)
print q
print "exact",exact
print "Actual error:", q[0]-exact
xlabel("Where integrand evaluated"); ylabel("order of evaluation")
show()


















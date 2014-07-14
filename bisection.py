def bisect(f,a,b,*args):#Use bisection search in order to find the root of a function.
    c = (a+b)/2.
    eps = 4*(2.**-52) #Allowed difference 
    if args == True: tol = args[0]
    else: tol = eps
    #Root-finding calculation
    from numpy import sign
    try:
        assert sign(f(a))!=sign(f(b))
        while abs((b-a)/2.)>=tol:
            c = (a+b)/2.
            if sign(f(c))!=sign(f(b)):
                a = c
            else:
                b = c
        return '%.16f'%(c)

    except AssertionError:
        print '''You didn't give me a bracket!
Go back to the Intermediate Value Theorem.'''

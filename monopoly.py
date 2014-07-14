def monopoly(c,x):
    n = len(c)
    if n == 1:
        return c[0] # If only constant term
    elif n == 2:
        return c[0]+c[1]*x #Base case 
    else:
        return c[0]+x*monopoly(c[1:],x) #Recursive call
    

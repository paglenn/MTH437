def MSRNG(N):
    r = empty(N)
    x = empty(N)
    m = 2.**31 - 1.
    a = 16807
    x[-1] = time()
    for i in range(N):
        x[i] = (a*x[i-1])%m
        r[i] = float(x[i])/m
    return r

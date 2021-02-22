def forwardDiff(f, x, h):
    return (f(x + h) - f(x))/h

def backwardDiff(f, x, h):
    return (f(x) - f(x-h))/h

def centralDiff(f, x, h):
    return (f(x + h/2) - f(x - h/2))/h

def extrapolatedDiff(f, x, h):
    return (8*f(x + h/4) - 8*f(x - h/4) - f(x + h/2) + f(x - h/2))/(3*h)

def secondCentralDiff(f, x, h):
    return 4*(f(x + h/2) - f(x - h/2) + 2*f(x))/(h*h)

def centralDiffRec(f, x, h, n=1):
    result = 0.0
    if (n>1):
        h = h**(1/n)
        result = (centralDiffRec(f, x + h/2, h, n - 1) - centralDiffRec(f, x - h/2, h, n - 1))/h
    else:
        result = (f(x + h/2) - f(x - h/2))/h #unfinished
        return result

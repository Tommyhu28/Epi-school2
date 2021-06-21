import numpy as numpy

def solve_quadratic(a,b,c):
    rad = (b**2 - 4*a*c)**0.5
    neg = -b
    denom = 2*a
    if (numpy.iscomplex(rad)):
        return None
    root1= (neg+rad)/denom
    root2= (neg-rad)/denom
    if (root1 != root2):
        return print((root1,root2))
    else:
        return print(root1)


# solve_quadratic(1,0,1)
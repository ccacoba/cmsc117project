"""
    This contains Composite Newton Cotes Quadrature.
    The function CompNCQuad requires inputs as following:
        f - the function to integrate.
        a - the lower limit of integration.
        b - the upper limit of integration.
        m - the number of subdivisions.
        n - the degree of the Lagrange polynomial.
"""

import base
from base import *

def CompNCQuad(f,a,b,m,n):
    w = NCQweights(n)
    h = (b-a)/(m*n)
    F = [0 for i in range(n+1)]
    for j in range(n+1):
        for i in range(m):
            x = a + (n*i+j)*h
            F[j] = F[j] + f(x)
    I = sdot(h,F)
    I = vdot(I,w)
    return I

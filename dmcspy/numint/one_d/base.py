"""
Base.py file:
    Contains functions used in Numerical integration such as weight finding and
    post processing.
"""
from ..__init__ import linalg

def NCQweights(n):
    b = [0 for i in range(1,n+2,1)]
    A = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):
        A[0][i] = 1
    for i in range(n+1):
        b[i] = (n**(i+1))/(i+1)
    for k in range(1,n+1,1):
        for j in range(n+1):
            A[k][j] = j**k
    w, time = linalg.direct.gem.gem_solve(A,b)
    return w

def sdot(s,v):
    sum = 0
    for i in range(len(v)):
        sum += v[i]*s
    return sum

def vdot(v1,v2):
    sum = 0
    for i in range(len(v1)):
        sum += v1[i]*v2[i]
    return sum


"""
This is module system in dmcspy.root.

This module includes an implementation of the
Newton Method for solving a system of nonlinear
equations. 
"""
__author__ = 'Riyana Gueco'
from time import time
import numpy as np

def Newton(F, J, x, maxit=100, tol=1e-10):
    """
    A method that solves a system of nonlinear equations.

    Arguments:
        F       - system of nonlinear equations
        J       - the Jacobian of F 
        x       - initial value
        maxit   - maximum number of iterations 
        tol     - tolerance value

    Returns:
        x               - solution
        (end-start)     - time elapsed
        i               - number of iterations
    """
    
    # Start timer
    start = time()  

    # Initialize variables
    F_x = F(x)
    F_norm = np.linalg.norm(F_x, ord=2)  # l2 norm of vector
    
    i = 0
    while abs(F_norm) > tol and i < maxit:
        delta = np.linalg.solve(J(x), -F_x)
        x = x + delta
        F_x = F(x)
        F_norm = np.linalg.norm(F_x, ord=2)
        i += 1

    # Too many iterations
    if abs(F_norm) > tol:
        print('Too many iterations!')
    end = time()
    return x, (end-start), i
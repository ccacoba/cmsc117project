"""
This is a module under dmcs.linalg.iterative.

This module includes the implementation of Jacobian Over Relaxation method for approximating the solutions of a system given the Matrix 'A', the Matrix 'A', and the initial solution 'x'.

Iterative methods are more efficient to use when the system is large, i.e. the number of equations is beyond the capacity of manual solving.
"""
import numpy as np
from time import time

__author__ = 'Charles Nikkon Acoba'
def jor_solve(A, b, x, tol = 1e-12, M = 100, w = 1.25):
	"""
	A function that executes the JOR Method to approximate the solutions of the system
	Arguments:
		A 	- the Matrix form of the system Ax = b
		b 	- the Vector b in the system Ax = b
		x 	- the initial guess
		tol 	- tolerance
		M	- the number of iterations
		w	- the value of the relaxation
	Return:
		x 		- approximation of x such that Ax=b
		(end-start)	- time elapsed
		i 		- number of iterations
	"""
	start = time()
	n = len(A)
	A = np.array(A)
	b = np.array(b)
	x = np.array(x)
	it =0
	
	error = np.linalg.norm(np.dot(A,x) - b) / np.linalg.norm(b)
	while error > tol and it < M :
		it = it + 1
		x_temp = x
		for i in range(n):
			s = 0
			for j in range(n):
				if j != i:
					s += A[i][j]*x_temp[j]
			x[i] = w*(b[i] - s)/A[i][i] + (1-w)*x_temp[i]
		error = np.linalg.norm(np.dot(A,x) - b) / np.linalg.norm(b)
	end = time()
	return x, end-start, it

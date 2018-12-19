"""
This is a module under dmcs.linalg.direct.

This module includes the implementation of forward substitution method for solving the solutions of a system given the lower triangular matrix 'L', the vector 'b'.

"""
__author__ = 'Charles Nikkon Acoba'
from time import time
def fwdward(L, b):
	"""
	A function that solves the linear system Ly=b where
	L is a lower triangular matrix and b is a vector.
	
	Arguments:
		L 	- lower triangular matrix form of the system Ly = b
		b 	- the Vector b in the system Ax = b

	Return:
		x 		- approximation of x such that Ax=b
		(end-start)	- time elapsed
			
	"""
	start = time()
	#Solves the linear system Lx=b where
	# L is a lower triangular matrix and b is a vector.
	start = time()
	n = len(b) 
	#initialize x
	x = [0 for k in range(n)] 
	#list with 0 of n Components.
	x[0] = b[0]/ L[0][0]
	for j in range(1, n):
		x[j] = (b[j] - sum(L[j][i]*x[i] for i in range(j))) / L[j][j]
	end = time()
	runtime = end - start
	return x, runtime
	
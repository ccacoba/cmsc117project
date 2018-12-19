"""
This is a module under dmcs.linalg.direct.

This module includes the implementation of backward substitution method for solving the solutions of a system given the Upper triangular matrix 'U', the vector 'b'.

"""
from time import time
__author__ = 'Charles Nikkon Acoba'
def bckward(U, b):
	"""
	A function that solves the linear system Ux=b where
	U is a upper triangular matrix and b is a vector.
	
	Arguments:
		U 	- upper triangular matrix form of the system Ux = b
		b 	- the Vector b in the system Ax = b

	Return:
		x 		- approximation of x such that Ax=b
		(end-start)	- time elapsed
			
	"""
	#Solves the linear system Ux=b where
	# U is a upper triangular matrix and b is a vector.
	
	start = time()
	n = len(b) 
	#initialize x	
	x = [0 for k in range(n)] 
	#list with 0 of n Components.
	x[n-1] = b[n-1]/ U[n-1][n-1]
	for j in range(n-2, -1, -1):
		x[j] = (b[j] - sum(U[j][i]*x[i] for i in range(j+1, n))) / U[j][j]
	end = time()
	return x, (end- start)
	

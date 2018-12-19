"""
This is a module under dmcs.linalg.direct.

This module includes the implementation of LU Decomposition methods (Doolittle, kji, jki, partial) which will be needed for solving the solutions of the system Ax = b. 

This module split A into L (a lower triangular matrix), U (a upper triangular matrix).


"""
__author__ = 'Charles Nikkon Acoba'
from copy import deepcopy
from time import time

def LU_doolittle(A):
	"""
	A function that split A into L, U.
	
	Arguments:
		A - the matrix for of the system Ax = b

	Return:
		L 		- the lower triangular matrix of A
		U 		- the upper triangular matrix of A
		(end-start)	- time elapsed
			
	"""
	start = time()
	n = len(A)
	L = [[0 for k in range(n)] for k in range(n)]	
	U = [[0 for k in range(n)] for k in range(n)]	
	
	for i in range(n):
		for k in range(i,n):
			sum = 0
			for j in range(i):
				sum += (L[i][j] * U[j][k])
			U[i][k] = A[i][k] - sum
		for k in range(i, n):
			if i==k :
				L[i][i] = 1
			else:
				sum = 0
				for j in range(i):
					sum += (L[k][j]*U[j][i])
				L[k][i] = (A[k][i] - sum)/U[i][i]
	end = time()
	return L, U, start - end
def LU_kji(A):
	"""
	A function that partitions A into L, U.
	
	Arguments:
		A - the matrix for of the system Ax = b

	Return:
		L 		- the lower triangular matrix of A
		U 		- the upper triangular matrix of A
		(end-start)	- time elapsed
			
	"""
	start = time()
	n = len(A)
	A = deepcopy(A)
	#kji version
	for k in range(n-1):
		for j in range(k+1, n):
			A[j][k] = A[j][k]/A[k][k]
		for j in range(k+1, n):
			for i in range(k+1, n):
				A[i][j] = A[i][j] - A[i][k]*A[k][j]
	L = [[0.0 for k in range(n)] for k in range(n)]
	U = [[0.0 for k in range(n)] for k in range(n)]
	
	for k in range(n):
		L[k][k] = 1.0
	for row in range(n):
		for col in range(n):
			if col >= row:
				U[row][col] = A[row][col]
			else:
				L[row][col] = A[row][col]
	end = time()
	return L, U, start - end

def LU_jki(A):
	"""
	A function that partitions A into L, U.
	
	Arguments:
		A - the matrix for of the system Ax = b

	Return:
		L 		- the lower triangular matrix of A
		U 		- the upper triangular matrix of A
		(end-start)	- time elapsed
			
	"""
	start = time()
	n = len(A)
	A = deepcopy(A)
	for j in range(n):
		for k in range(j):
			for i in range(k+1, n):
				A[i][j] = A[i][j] - A[i][k]*A[k][j]
		for i in range(j+1, n):
			A[i][j] = A[i][j]/A[j][j]
	L = [[0.0 for k in range(n)] for k in range(n)]
	U = [[0.0 for k in range(n)] for k in range(n)]
	
	for k in range(n):
		L[k][k] = 1.0
	for row in range(n):
		for col in range(n):
			if col >= row:
				U[row][col] = A[row][col]
			else:
				L[row][col] = A[row][col]
	end = time()
	return L, U, start - end
	
def LU_partial(A):
	"""
	A function that partitions A into L, U.
	Used when the pivot/s is/are 0.
	
	Arguments:
		A - the matrix for of the system Ax = b

	Return:
		L 		- the lower triangular matrix of A
		U 		- the upper triangular matrix of A
		p		- changes in position of A
		(end-start)	- time elapsed
			
	"""
	start = time()
	n = len(A)
	A = deepcopy(A)
	p = [i for i in range(n)]
	l = [i for i in range(n)]
	for k in range(n-1):
		if A[k][k] == 0:
			m = abs(A[k][k])
			l = k
			#finds the max in the kth column
			for r in range(k+1,n):
				if abs(A[r][k]) > m :
					m= A[r][k]
					l=r
			#swaps the position in p
			p[k], p[l] = p[l], p[k]
			#swaps the position in A
			A[k], A[l] = A[l], A[k]
			
	for k in range(n-1):
		for j in range(k+1, n):
			A[j][k] = A[j][k]/A[k][k]
		for j in range(k+1, n):
			for i in range(k+1, n):
				A[i][j] = A[i][j] - A[i][k]*A[k][j]
	L = [[0.0 for k in range(n)] for k in range(n)]
	U = [[0.0 for k in range(n)] for k in range(n)]
	
	for k in range(n):
		L[k][k] = 1.0
	for row in range(n):
		for col in range(n):
			if col >= row:
				U[row][col] = A[row][col]
			else:
				L[row][col] = A[row][col]
	
	end = time()
	return L, U, p,start - end


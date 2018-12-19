"""
This is a module under dmcs.linalg.direct.

This module includes the implementation of LU Solving methods (Doolittle, kji, jki, partial) which solves the solutions of the system Ax = b. 


"""
from .backward import bckward as bckSub
from .forward import fwdward as fwdSub
from .lu import LU_doolittle 
from .lu import LU_kji
from .lu import LU_jki
from .lu import LU_partial
from time import time
__author__ = 'Charles Nikkon Acoba'

def LU_solve_doolittle(A, b):
	"""
	A function that solves the linear system Ax=b where
	A is a matrix and b is a vector by spliting A into L, U then using forward and backward subtitution.
	
	Arguments:
		A 	- A matrix form of the system Ax = b
		b 	- the Vector b in the system Ax = b

	Return:
		x 		- approximation of x such that Ax=b
		(end-start)	- time elapsed
			
	"""
#LU factorization
	start = time()
	L, U, place = LU_doolittle(A)
	
	newY, place = fwdSub(L,b)
	newX, place = bckSub(U,newY)
	end = time()
	return newX, end - start

def LU_solve_kji(A, b):
	"""
	A function that solves the linear system Ax=b where
	A is a matrix and b is a vector by spliting A into L, U then using forward and backward subtitution.
	
	Arguments:
		A 	- A matrix form of the system Ax = b
		b 	- the Vector b in the system Ax = b

	Return:
		x 		- approximation of x such that Ax=b
		(end-start)	- time elapsed
			
	"""
#LU factorization
	start = time()
	L, U, place = LU_kji(A)
	
	newY, place = fwdSub(L,b)
	newX, place = bckSub(U,newY)
	end = time()
	return newX, end - start
def LU_solve_jki(A, b):
	"""
	A function that solves the linear system Ax=b where
	A is a matrix and b is a vector by spliting A into L, U then using forward and backward subtitution.
	
	Arguments:
		A 	- A matrix form of the system Ax = b
		b 	- the Vector b in the system Ax = b

	Return:
		x 		- approximation of x such that Ax=b
		(end-start)	- time elapsed
			
	"""
#LU factorization
	start = time()
	L, U, place = LU_jki(A)
	newY, place = fwdSub(L,b)
	newX, place = bckSub(U,newY)
	end = time()
	return newX, end - start
	
def LU_solve_partial(A, b):
	"""
	A function that solves the linear system Ax=b where
	A is a matrix and b is a vector by spliting A into L, U then using forward and backward subtitution.
	This function is used when A has a pivot that is 0.
	
	Arguments:
		A 	- A matrix form of the system Ax = b
		b 	- the Vector b in the system Ax = b

	Return:
		x 		- approximation of x such that Ax=b
		(end-start)	- time elapsed
			
	"""
	start = time()
	n = len(A)
	L, U, p, place = LU_partial(A)
	
	for j in range(n):
		b[p[j]] = b[j]
	
	newY, place = fwdSub(L,b)
	newX, place = bckSub(U,newY)
	end = time()
	return newX, end - start

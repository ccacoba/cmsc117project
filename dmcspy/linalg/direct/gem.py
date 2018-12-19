import numpy as np
from copy import deepcopy
from .backward import bckward as backward
from time import time
def gem_solve(A, b):
	start = time()
	n = len(A)
	U = [[0.0 for k in range(n)] for k in range(n)]
	for k in range(n):
		for i in range(k+1,n):
			A[i][k] = A[i][k]/A[k][k]
			b[i] = b[i] - A[i][k]*b[k]
		for j in range(k+1,n):
			for i in range(k+1, n):
				A[i][j] = A[i][j]-A[i][k]*A[k][j]
				
	for i in range(n):
		for j in range(n):
			if i>j:
				U[i][j] = 0
			else:
				U[i][j] = A[i][j]
	
	x, place = backward(U, b)
	end = time()
	return x, (end-start)


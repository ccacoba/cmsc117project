from .backward import bckward as bckSub
from .forward import fwdward as fwdSub
from .lu import LU_doolittle 
from .lu import LU_kji
from .lu import LU_jki
from .lu import LU_partial
from time import time


def LU_solve_doolittle(A, b):
#LU factorization
	start = time()
	L, U, place = LU_doolittle(A)
	
	newY, place = fwdSub(L,b)
	newX, place = bckSub(U,newY)
	end = time()
	return newX, end - start

def LU_solve_kji(A, b):
#LU factorization
	start = time()
	L, U, place = LU_kji(A)
	
	newY, place = fwdSub(L,b)
	newX, place = bckSub(U,newY)
	end = time()
	return newX, end - start
def LU_solve_jki(A, b):
#LU factorization
	start = time()
	L, U, place = LU_jki(A)
	newY, place = fwdSub(L,b)
	newX, place = bckSub(U,newY)
	end = time()
	return newX, end - start
	
def LU_solve_partial(A, b):
	start = time()
	n = len(A)
	L, U, p, place = LU_partial(A)
	
	for j in range(n):
		b[p[j]] = b[j]
	
	newY, place = fwdSub(L,b)
	newX, place = bckSub(U,newY)
	end = time()
	return newX, end - start

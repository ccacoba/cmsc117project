# ------------------------------------------ #
# -------- EXAMPLES FOR LINALG ------------- #
# -------------by Nikkon Acoba-------------- #
from ..linalg import *
from ..root import *
from ..numdiff import *
import numpy as np

def linalg_bckSub():
	print("---BACKWARD SUBSTITUTION METHOD---\n")
	Upp = [[1, -2, 1], [0,1,6], [0,0,1]]
	b = [4,-1,2]
	print("Upper Triangular Matrix: ", Upp)
	print("Vector b: ", b)
	print(" ")
	x_val, time_val = direct.backward.bckward(Upp, b)
	base.PrintResults1(x_val, time_val)
	
def linalg_fwdSub():
	print("---FORWARD SUBSTITUTION METHOD---\n")
	Low = [[2, 0, 0], [3,5,0], [7,8,9]]
	b = [2,8,24]
	print("Lower Triangular Matrix: ", Low)
	print("Vector b: ", b)
	print(" ")
	x_val, time_val = direct.forward.fwdward(Low, b)
	base.PrintResults1(x_val, time_val)

def linalg_gem_solve():
	print("---GAUSSIAN ELIMANATION METHOD---\n")
	A = [[1,1,-1],[1,-2,3],[2,3,1]]
	b = [4,-6,7]
	print("Matrix: \n", A)
	print("Vector b: \n", b)
	print(" ")
	x_val, time_val = direct.gem.gem_solve(A, b)
	base.PrintResults1(x_val, time_val)	
def linalg_LU():
	A = [[1,1,-1],[1,-2,3],[2,3,1]]
	print("---LU Decomposition METHODS---\n")
	print("Matrix 'A'\n ", A)
	
	print(" ")
	print("--Doolittle Method--\n")
	L, U, time_val = direct.lu.LU_doolittle(A)
	print("Lower Triangular Matrix: \n", L)
	print("Upper Triangular Matrix: \n", U)
	print("Time Elapsed: ", time_val)
	print(" ")
	print("--KJI Method--\n")
	L,U, time_val = direct.lu.LU_kji(A)
	print("Lower Triangular Matrix: \n", L)
	print("Upper Triangular Matrix: \n", U)
	print("Time Elapsed: ", time_val)
	print(" ")
	print("--JKI Method--\n")
	L,U, time_val = direct.lu.LU_kji(A)
	print("Lower Triangular Matrix: \n", L)
	print("Upper Triangular Matrix: \n", U)
	print("Time Elapsed: ", time_val)
	print(" ")
def linalg_LU_partial():
	A = [[0,1,-1],[1,-2,3],[2,3,1]]
	print("---LU Partial Decomposition Method---\n")
	print("Matrix 'A'\n ", A)
	L,U,p ,time_val = direct.lu.LU_partial(A)
	print("Lower Triangular Matrix: \n", L)
	print("Upper Triangular Matrix: \n", U)
	print("Changes in position: \n", p)
	print("Time Elapsed: ", time_val)
	print(" ")
def linalg_LU_solve():
	print("---LU SOLVING METHODS---\n")
	A = [[1,1,-1],[1,-2,3],[2,3,1]]
	b = [4,-6,7]
	print("Matrix: \n", A)
	print("Vector b: \n", b)
	print(" ")
	print("---LU Doolittle solving method---\n")
	x_val, time_val = direct.lusolve.LU_solve_doolittle(A, b)
	base.PrintResults1(x_val, time_val)	
	print(" ")
	print("---LU kji solving method---\n")
	x_val, time_val = direct.lusolve.LU_solve_kji(A, b)
	base.PrintResults1(x_val, time_val)	
	print(" ")
	print("---LU jki solving method---\n")
	x_val, time_val = direct.lusolve.LU_solve_jki(A, b)
	base.PrintResults1(x_val, time_val)	
def linalg_LU_partial_solve():
	A = [[0,1,-1],[1,-2,3],[2,3,1]]
	b = [4,-6,7]
	print("Matrix: \n", A)
	print("Vector b: \n", b)
	print(" ")
	print("---LU partial solving method---\n")
	x_val, time_val = direct.lusolve.LU_solve_partial(A, b)
	base.PrintResults1(x_val, time_val)	
def linalg_sor():
	A = [[4,3,0],[3,4,-1],[0,-1,4]]
	b = [24,30,-24]
	x0 = [1,1,1]
	print("---SOR METHOD---\n")
	print("Matrix 'A'\n ", A)
	print("Vector 'b': ", b)
	print("Intitial guess 'x0': ",x0)
	print(" ")
	x_val, time_val, iters_val = iterative.sor.sor_solve(A, b, x0, tol = 1e-12, M = 100, w = 1.25)
	base.PrintResults(x_val, time_val, iters_val)
	#INPUT THE SIZE OF A MATRIX
	n = 5
	#---
	
	A = np.random.randint(9, size =(n,n))
	b = np.random.randint(9, size=(n))
	x0 = np.ones(n)
	print("Matrix 'A'\n ", A)
	print("Vector 'b': ", b)
	print("Intitial guess 'x0': ",x0)
	print(" ")
	x_val, time_val, iters_val = iterative.sor.sor_solve(A, b, x0, tol = 1e-12, M = 100, w = 1.25)
	base.PrintResults(x_val, time_val, iters_val)

def linalg_jor():
	A = [[4,3,0],[3,4,-1],[0,-1,4]]
	b = [24,30,-24]
	x0 = [1,1,1]
	print("---JOR METHOD---\n")
	print("Matrix 'A'\n ", A)
	print("Vector 'b': ", b)
	print("Intitial guess 'x0': ",x0)
	print(" ")
	x_val, time_val, iters_val = iterative.jor.jor_solve(A, b, x0, tol = 1e-12, M = 100, w = 1.25)
	base.PrintResults(x_val, time_val, iters_val)
	#INPUT THE SIZE OF A MATRIX
	n = 5
	#---
	A = np.random.randint(9, size =(n,n))
	b = np.random.randint(9, size=(n))
	x0 = np.ones(n)
	print("Matrix 'A'\n	 ", A)
	print("Vector 'b': ", b)
	print("Intitial guess 'x0': ",x0)
	print(" ")
	x_val, time_val, iters_val = iterative.jor.jor_solve(A, b, x0, tol = 1e-12, M = 100, w = 1.25)
	base.PrintResults(x_val, time_val, iters_val)

	

	
# ------------------------------------------ #
# -------- EXAMPLES FOR scalar.py ---------- #
# ------------ Riyana Gueco ---------------- #
# ------------------------------------------ #

def f(x):
	"""
	A function to represent f(x) = cos^2(2x)-x^2
	"""
	return np.cos(2*x)**2-(x**2)

def df(x):
	"""
	A function to represent the derivative of f(x) = cos^2(2x)-x^2
	"""
	return -2*(np.sin(4*x)+x)

def BisectionMethodExample(f=f):
	print("BISECTION METHOD: f(x) = cos^2(2x) - x^2")
	x_val, time_val, iters_val = scalar.BisectionMethod(f)
	base.PrintResults(x_val, time_val, iters_val)
	print("Value of f(x): ", end='')
	print(f(x_val))

	print(" ")

def SecantMethodExample(f=f):
	print("SECANT METHOD: f(x) = cos^2(2x) - x^2")
	x_val, time_val, iters_val = scalar.SecantMethod(f)
	base.PrintResults(x_val, time_val, iters_val)
	print("Value of f(x): ", end='')
	print(f(x_val))

	print(" ")

def NewtonMethodExample(f=f, df=df):
	print("NEWTON METHOD: f(x) = cos^2(2x) - x^2")
	x_val, time_val, iters_val = scalar.NewtonMethod(f, df)
	base.PrintResults(x_val, time_val, iters_val)
	print("Value of f(x): ", end='')
	print(f(x_val))

	print(" ")

def ChordMethodExample(f=f):
	print("CHORD METHOD: f(x) = cos^2(2x) - x^2")
	x_val, time_val, iters_val = scalar.ChordMethod(f)
	base.PrintResults(x_val, time_val, iters_val)
	print("Value of f(x): ", end='')
	print(f(x_val))

	print(" ")

def RegulaFalsiMethodExample(f=f):
	print("REGULA-FALSI METHOD: f(x) = cos^2(2x) - x^2")
	x_val, time_val, iters_val = scalar.RegulaFalsiMethod(f)
	base.PrintResults(x_val, time_val, iters_val)
	print("Value of f(x): ", end='')
	print(f(x_val))

	print(" ")


# ------------------------------------------ #
# -------- EXAMPLES FOR poly.py ------------ #
# ----------- Riyana Gueco ----------------- #
# ------------------------------------------ #

def F(x):
	return 1+x**2+x**3

def NewtonHornerExample(F=F):
	a = [1., 1., 1.]
	print("NEWTON-HORNER METHOD: f(x) = 1 + x^2 + x^3")
	x_val, time_val, iters_val = poly.NewtonHorner(a, 0.5, ref=False)
	base.PrintResults(x_val, time_val, iters_val)
	print("Value of f(x): ", end='')
	print([F(x) for x in x_val])

	print(" ")
# ------------------------------------------ #
# -------- EXAMPLES FOR NUMDIFF ------------ #
# ------------------------------------------ #
def numdiff_forward():
	print("--FORWARD DIFFERENCE METHOD--")
	time=first.forward_difference()
	print("Time Elapsed: ", time)
	print(" ")
def numdiff_backward():
	print("--BACKWARD DIFFERENCE METHOD--")
	time=first.backward_difference()
	print("Time Elapsed: ", time)
	print(" ")
def numdiff_center():
	print("--BACKWARD DIFFERENCE METHOD--")
	time=first.center_difference()
	print("Time Elapsed: ", time)
	print(" ")	
def numdiff_second_derivative():
	print("--Second derivative METHOD--")
	time=second.second_derivative()
	print("Time Elapsed: ", time)
	print(" ")	

if __name__ == '__main__':
	linalg_bckSub() #calling backward substitution example
	linalg_fwdSub()	#calling forward substitution example
	linalg_gem_solve() #calling GEM
	linalg_LU() # calling LU decomposition methods example
	linalg_LU_partial() # calling LU Partial Decomposition example
	linalg_LU_solve() #calling LU Solving methods
	linalg_LU_partial_solve() #calling LU partial Solving method
	linalg_sor() #calling sor
	linalg_jor() #calling jor
	BisectionMethodExample()
	SecantMethodExample()
	NewtonMethodExample()
	ChordMethodExample()
	RegulaFalsiMethodExample()
	NewtonHornerExample()
	numdiff_forward()
	numdiff_backward()
	numdiff_center()
	numdiff_second_derivative()

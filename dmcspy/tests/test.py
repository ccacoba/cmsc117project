# ------------------------------------------ #
# -------- EXAMPLES FOR scalar.py ---------- #
# ------------------------------------------ #
from ..root import *
import numpy as np
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
"""
This is module scalar under dmcspy.root.

This module includes the implementation of various methods
for approximating the zero/s of a given function. Methods included
are the following:

Bisection Method
------------------------------------------------------------------
The Bisection Method is a successive approximation method
that narrows down an interval [a, b] containing the root of a
function f by repeatedly setting either a or b to the bisection
of [a, b]. The resulting interval should be extremely small.
(www.mathcs.emory.edu)

Secant Method
------------------------------------------------------------------
The Secant Method assumes that the region of interest (the region
containing the root) is approximately linear. In each iteration, 
the point where the approximating line crosses the axis is taken into 
consideration. 
(mathworld.worlfram.com)

Newton Method
------------------------------------------------------------------
The Newton Method uses the first few terms of the Taylor series of
a function f in the vicinity of an initial guess of the root. 
(mathworld.worlfram.com)

Chord Method 
------------------------------------------------------------------
The Chord Method is a combination of the Newton Method and the Secant
Method. The bisection of an interval [a, b] is mapped to a point on the 
line and is used as the new candidate for x.

Regula-Falsi Method 
------------------------------------------------------------------
The Regula-Falsi Method, or False Position Method, is an improvement 
on the Bisection Method. Instead of looking for an interval [a, b] small 
enough for the approximation of x, we will instead take into consideration 
the straight line joining (a, f(a)) and (b, f(b)) and take the x-intercept 
as our next guess.
(mat.iitm.ac.in)
"""
__author__ = 'Riyana Gueco'
from time import time
import numpy as np
def BisectionMethod(f, a=0, b=1, tol=1e-10):
	"""
	A function that executes the bisection method to approximate
	the zero/s of a function f.

	Arguments:
		f 	- function
		a 	- left endpoint
		b 	- right endpoint
		tol 	- tolerance
	Return:
		c 		- approximation of x such that f(x) = 0 
		(end-start) 	- time elapsed 
		i 		- number of iterations
	"""
	start = time()
	f_a = f(a)
	f_b = f(b)
	
	# Initialization of errors and iters
	errs = []
	i = 0

	if f_a == 0:
		return a
	elif f_b == 0:
		return b
	elif f_a*f_b > 0:
		print("The function values have the same sign!")
	else:
		error = b-a
		while error > tol:
			c = (b+a)/2
			f_c = f(c)
			
			errs.append(error)
			
			if f_a*f_c > 0:
				a = c
				f_a = f_c
			elif f_a*f_c < 0:
				b = c
				f_b = f_c
			else:
				break
			error = b-a
			i = i+1
	end = time()
	return c, (end-start), i

def SecantMethod(f, x_0=0.0, x_1=0.75, tol=1e-10):
	"""
	A function that executes the Secant Method to approximate
	the zero/s of a function f.

	Arguments:
		f 	- function
		x_0 	- first point
		x_1 	- second point
		tol 	- tolerance
	Return:
		x_1 		- approximation of x such that f(x) = 0 
		(end-start)	- time elapsed
		i 		- number of iterations
	"""
	start = time()
	f_0 = f(x_0)
	f_1 = f(x_1)
	error = np.abs(x_0-x_1)
	
	i = 0
	errs = []
	
	while error > tol:
		errs.append(error)

		slope = (f_1 - f_0) / (x_1 - x_0)
		x_0 = x_1
		x_1 = x_1 - f_1 / slope
		error = np.abs(x_0-x_1)
		f_0 = f_1
		f_1 = f(x_1)
		i = i+1
	end = time()
	return x_1, (end-start), i

def NewtonMethod(f, df, x=0.75, tol=1e-10):
	"""
	A function that executes the Newton Method to approximate
	the zero/s of a function f.

	Arguments:
		f 	- function
		df 	- derivative of f
		x 	- initial guess
		tol 	- tolerance
	Return:
		x 		- an approximation of x such that f(x) = 0
		(end-start) 	- time elapsed
		i 		- number of iterations
	"""
	start = time()
	error = tol + 1
	
	i = 0
	errs = []

	while error > tol:
		errs.append(error)

		x_temp = x
		x = x - f(x) / df(x)
		error = np.abs(x-x_temp)
		i = i+1
	end = time()
	return x, (end-start), i

def ChordMethod(f, a=0.0, b=1.0, x=0.75, tol=1e-10):
	"""
	A function that executes the Chord Method to approximate
	the zero/s of a function f.

	Arguments:
		f 	- function
		a 	- left endpoint
		b 	- right endpoint
		x 	- initial point
		tol 	- tolerance

	Return:
		x 		- roots of f 
		(end-start) 	- time elapsed
		i 		- number of iterations
	"""
	start = time()

	# Initialization of function values and error 
	f_a = f(a)
	f_b = f(b)
	f_x = f(x)
	error = np.abs(f_x)

	# Initialization of iter number and array of error values
	i = 0
	errs = []

	if f_a*f_b<0:
		while error > tol:
			errs.append(error)

			if f_a*f_x < 0:
				x = (x*f_a - a*f_x) / (f_a - f_x)
			else:
				x = (x*f_b - b*f_x) / (f_b - f_x)

			f_x = f(x)
			error = np.abs(f_x)
			i = i+1
	else:
		print("Function values are of the same sign!")
	end = time()
	return x, (end-start), i

def RegulaFalsiMethod(f, a=0.0, b=0.75, tol=1e-10):
	"""
	A function that executes the Regula-Falsi Method to approximate
	the zero/s of a function f.

	Arguments:
		f 	- function
		a 	- first point
		b 	- second point
		tol 	- tolerance
	Return:
		x 		- approximation of x where f(x) = 0
		(end-start) 	- time elapsed 
		i 		- number of iterations
	"""
	start = time()
	f_a = f(a)
	f_b = f(b)
	error = tol + 1
	
	errs = []
	i = 0

	while error > tol:
		x = (a*f_b - b*f_a) / (f_b - f_a)
		f_x = f(x)

		errs.append(error)

		if f_a*f_x > 0:
			a = x
			f_a = f_x
		elif f_b*f_x > 0:
			b = x
			f_b = f_x
		else:
			break

		error = np.abs(f_x)
		i = i+1
	end = time()
	return x, (end-start), i
"""
This is module poly under dmcspy.root.

This module includes the implementation of Newton-Horner
method in root-finding for polynomial functions.
"""
__author__ = 'Riyana Gueco'
from time import time
def Horner(a, z):
	"""
	A function that evaluates the value of a (complex) number
	uner a polynomial function.

	Arguments:
		- a 	list of coefficients of the polynomial in descending
				power so that a[0] is he coefficient of the leading
				term
		- z		(complex) number

	Returns:
		- b[-1]	value of the polynomial at point z
		- b		list of coefficients of the quotient
	"""
	n = len(a)
	b = [0.0] * n
	b[0] = a[0]
	for k in range(1, n):
		b[k] = a[k] + b[k-1] * z
	return b[-1], b
	
def NewtonHorner(a, z, tol=1e-10, maxit=100, ref=False, maxref=100):
	"""
	A function that approximates the root/zeros of a polynomial
	function.

	Arguments:
		- a 		list of coefficients
		- z 		initial point
		- tol 		tolerance (default 1e-10)
		- maxit		maximum number of iterations (default 100)
		- ref		boolean variable for refinement (default false)
		- maxref	maximum number of iterations in refinement

	Returns:
		- 		(complex) zeros of the given polynomial
		- 		time elapsed 
		- 		number of iterations
	"""

	start = time()

	# define mahine epsilon
	machine_eps = 7./3 - 4./3 - 1

	# initialize values
	a_start = a.copy()
	deg = len(a) - 1
	roots = []
	iters = []
	ref_iters = []
	
	for k in range(deg):
		it = 0
		z = z + complex(0, 1) * z 		# if z is real, write it in complex form
		error = tol + 1 				# define error greater than tolerance
		
		# for last iteration:
		if k == deg - 1: 
			it += 1
			z = -a[1] / a[0]
		# other iterations
		else:
			while error > tol and it < maxit:
				it += 1 						# increment number of iterations
				z_old = z 						# store previous value of z
				pz, qz = Horner(a, z) 			# retrieve 
				pprimez = Horner(qz[:-1], z)[0] # all in qz except last
				if abs(pprimez) > machine_eps:
					z = z - pz / pprimez
					error = abs(z-z_old)
				else:
					print("ERROR: Division by a very small number!")
					z = z_old
					error = 0
		a = qz[:-1].copy()
		
		# refinement steps
		itref = 0
		if ref:
			zref = z
			error = tol+1
			while error > tol * 1e-3 and itref < maxref:
				itref += 1
				pz, qz = Horner(a_start, zref)
				pprimez = Horner(qz[:-1], z)[0]
				if abs(pprimez) > machine_eps:
					zref_new = zref - pz / pprimez
					error = abs(zref - zref_new)
				else:
					print("ERROR: Division by a very small number!")
					zref_new = zref
					error = 0
			z = zref_new
		roots += [z]
		iters += [it]
		ref_iters += [itref]
	end = time()
	return roots, (end-start), iters
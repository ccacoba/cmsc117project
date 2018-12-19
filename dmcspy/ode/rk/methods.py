__author__ = 'Imman Narciso'
import numpy as np
from time import time

"""
The Runge-Kutta algorithm may be very crudely described as "Heun's Method on steroids."
It takes to extremes the idea of correcting the predicted value of the next solution point in the numerical solution.
(calculuslab.deltacollege.edu)
This module has the 2nd and 4th oreder Runge Kutta methods.

Arguments:
        T           -   Final time  
        N           -   Number of steps
        function    -   function f used
        init        -   initial value x0

Output:
        x           -   coordinates of the approximated first order degree differential equation
        time        -   process time
"""

def rk2(T, N, function, init):
        start = time()
	grid = np.linspace(0, T, N+1) #generates equally segmented values of t
	h = grid[1] - grid[0]
	size = len(init)#init.shape[0]
	#pre-allocation
	x = np.zeros((size, len(grid))) 
	x[:,0] = init
	print(x)
	for k in range(N):
		w1 = x[:, k]
		w2 = w1 + 0.5*h*f(w1)
		x[:, k+1] = x[:,k] + (h/4)*(2*f(w1) + 2*f(w2))
	end = time()
	t = end - start
	return x, t

def rk4(T, N, function, init):
        start = time()
	grid = np.linspace(0, T, N+1) #generates equally segmented values of t
	h = grid[1] - grid[0]
	size = len(init)#init.shape[0]
	#pre-allocation
	x = np.zeros((size, len(grid)))
	print('row size is = ')
	print(size)
	print('comlumn size is =')
	print(len(grid))
	x[:,0] = init
	for k in range(N):
		w1 = x[:, k]
		w2 = w1 + 0.5*h*f(w1)
		w3 = w1 + 0.5*h*f(w2)
		w4 = w1 + h*f(w3)
		x[:, k+1] = x[:,k] + (h/6)*(f(w1) + 2*f(w2) + 2*f(w3) + f(w4))
	end = time()
	t = end - start
	return x, t


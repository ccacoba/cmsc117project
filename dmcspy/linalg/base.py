from .direct import *
from .iterative import *

def PrintResults(x_val, time_val, iters_val, x=True, time=True, iters=True):
	"""
	A method that prints the results from the 
	corresponding root-finding method used.
	Arguments:
		x 		- boolean value for whether or not to print x
		time 	- boolean value for whether or not to print time 
		iters 	- boolean value for whether or not to print iters
	"""
	if x:
		print("Approximate value for x: ", end='')
		print(x_val)
	if time:
		print("Time elapsed: ", end='')
		print(time_val)
	if iters:
		print("Number of iterations: ", end='')
		print(iters_val)
	
def PrintResults1(x_val, time_val, x=True, time=True):
	"""
	A method that prints the results from the 
	corresponding root-finding method used.
	Arguments:
		x 		- boolean value for whether or not to print x
		time 	- boolean value for whether or not to print time 
		iters 	- boolean value for whether or not to print iters
	"""
	if x:
		print("Approximate value for x: ", end='')
		print(x_val)
	if time:
		print("Time elapsed: ", end='')
		print(time_val)
	
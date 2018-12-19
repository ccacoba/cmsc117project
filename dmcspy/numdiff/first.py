#credits: PAALAN
import numpy as np 
from matplotlib import pyplot as plt 
#plt.rc('text', usetex=True)
plt.rc('font', family='serif')
#machine epsilon
eps = np.finfo('float').eps #4/3
# stepsizes
h = np.array([0.1/(1.1**k) for k in range(500)])
#takes stepsizes greather than eps
#h = h[h>eps]
from time import time
def forward_difference():
	start = time()
	"""
	This function shows the graph of the Forward Difference Formula
	f'(x) ~= [f(x+h) - f(x)]/h. The	truncation error is (h/2)f"(eps).
	
	Variables:
		- eps 		machine epsilon equal to np.finfo('float').eps
		- h 		step size

	Output:
		1. Graph of Forward Difference Formula with line truncation error,
			predicted optimal h, and horizontal line(for reference)
	"""
	
	error = np.abs(1 - (np. exp(h)- 1)/h)
	fig = plt.figure()
	plt.loglog(h, error, color='blue', linewidth = 2.0, label = r'$|1 - (e^h-1)/h|$')
	plt.xlabel(r'$h$', fontsize=12)
	plt.title('Forward Difference Formula')
	
	plt.loglog(h, h/2,  color='red', linestyle = '--', linewidth = 2.0, label = r'$h/2$')
	plt.loglog(h, 2*eps/h, color = 'green', linestyle = '--', linewidth = 2.0, label = r'$2\epsilon/h$')
	plt.loglog([2.0*eps**0.5, 2.0*eps**0.5], [0.0,1.0], linewidth=2.0, label=r'predicted optimal $h$',linestyle= '--')
	plt.plot([0,10**-1],[10**-10,10**-10], label=r'horizontal line $y=10^{-10}$')
	plt.ylim(bottom=1e-12, top=1.0)
	plt.legend(loc = 'best', fontsize = 15)
	plt.xticks(fontsize = 14)
	plt.yticks(fontsize = 14)
	plt.gca().autoscale(enable = True, axis='x', tight =True)
	end = time()
	plt.show()
	return (end - start)
def center_difference():
	start = time()
	"""
	This function shows the graph of Centered Difference Formula
	f'(x) ~= [f(x+h) - f(x - h)]/(2h). The truncation error is
	((h^2)/6)f'"(eps).

	Variables:
		- eps 		machine epsilon equal to np.finfo('float').eps
		- h 		step size

	Output:
		1. Graph of Centered Difference Formula with line truncation error,
			predicted optimal h, and horizontal line(for reference)
	"""
	
	error = np.abs(1 - ( np.exp(h) - np.exp(-h) )/(2*h))
	fig = plt.figure()
	plt.loglog(h, error, color='blue', linewidth = 2.0, label = r'$|1 - (e^h - e^{-h} )/2h|$')
	plt.xlabel(r'$h$', fontsize=12)
	plt.title('Centered Difference Formula')

	plt.loglog(h, h**2/6,  color='red', linestyle = '--', linewidth = 2.0, label = r'$h^2/6$')
	plt.loglog(h, 2*eps/h, color = 'green', linestyle = '--', linewidth = 2.0, label = r'$2\epsilon/h$')
	plt.loglog([(3.0*eps)**(1./3), (3.0*eps)**(1./3)], [0.0,1.0], linewidth=2.0, label=r'predicted optimal $h$',linestyle= '--')
	plt.plot([0,10**-1],[10**-10,10**-10], label=r'horizontal line $y=10^{-10}$')
	plt.ylim(bottom=1e-12, top=2.0)
	plt.legend(loc = 'best', fontsize = 15)
	plt.xticks(fontsize = 14)
	plt.yticks(fontsize = 14)
	plt.gca().autoscale(enable = True, axis='x', tight =True)
	
	end = time()
	plt.show()
	return (end - start)
def backward_difference():
	start = time()
	"""
	This function shows the graph of Backward Difference Formula
	f'(x) ~= [f(x) - f(x-h)]/h. The truncation error is (h/2)f"(eps).

	Variables:
		- eps 		machine epsilon equal to np.finfo('float').eps
		- h 		step size

	Output:
		1. Graph of Backward Difference Formula with line truncation error,
			predicted optimal h, and horizontal line(for reference)
	"""

	error = np.abs(1 - ( 1 - np.exp(-h) )/(h))
	fig = plt.figure()
	plt.loglog(h, error, color='blue', linewidth = 2.0, label = r'$|1 - (1 - e^{-h} )/h|$')
	plt.xlabel(r'$h$', fontsize=12)
	plt.title('Backward Difference Formula')
	
	plt.loglog(h, h/2,  color='red', linestyle = '--', linewidth = 2.0, label = r'$h/2$')
	plt.loglog(h, 2*eps/h, color = 'green', linestyle = '--', linewidth = 2.0, label = r'$2\epsilon/h$')
	plt.loglog([2.0*eps**0.5, 2.0*eps**0.5], [0.0,1.0], linewidth=2.0, label=r'predicted optimal $h$',linestyle= '--')
	plt.plot([0,10**-1],[10**-10,10**-10], label=r'horizontal line $y=10^{-10}$')
	plt.ylim(bottom=1e-12, top=1.0)
	plt.legend(loc = 'best', fontsize = 15)
	plt.xticks(fontsize = 14)
	plt.yticks(fontsize = 14)
	plt.gca().autoscale(enable = True, axis='x', tight =True)
	end = time()
	plt.show()
	return (end - start)
	
#forward_difference()
#backward_difference()
#center_difference()


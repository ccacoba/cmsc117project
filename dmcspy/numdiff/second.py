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

def second_derivative():
	"""
	This function shows the graph of the Second Derivative Formula
	f"(x) = [f(x+h) - 2f(x) + f(x-h)]/(h^2). The truncation error
	is -(h^2/12)f""(eps).
	
	Variables:
		- eps 		machine epsilon equal to np.finfo('float').eps
		- h 		step size

	Output:
		1. Graph of Second Derivative Formula with line truncation error,
			predicted optimal h, and horizontal line(for reference)
	"""

	error = np.abs(1 - ( np.exp(h) - 2 + np.exp(-h) )/(h**2))
	fig = plt.figure()
	plt.loglog(h, error, color='blue', linewidth = 2.0, label = r'$|1 - (e^h - 2 + e^{-h} )/h^2|$')
	plt.xlabel(r'$h$', fontsize=12)
	plt.title('Second Derivative Formula')

	plt.loglog(h, h**2/12,  color='red', linestyle = '--', linewidth = 2.0, label = r'$h^2/12$')
	plt.loglog(h, 24*eps/(h**2), color = 'green', linestyle = '--', linewidth = 2.0, label = r'$24\epsilon/h^{1/2}$')
	plt.loglog([6.*(eps)**0.25, 6.*(eps)**0.25], [0.0,1.5], linewidth=2.0, label=r'predicted optimal $h$',linestyle= '--')
	plt.plot([0,10**-1],[10**-10,10**-10], label=r'horizontal line $y=10^{-10}$')
	plt.ylim(bottom=1e-12, top=2.0)
	plt.legend(loc = 'best', fontsize = 15)
	plt.xticks(fontsize = 14)
	plt.yticks(fontsize = 14)
	plt.gca().autoscale(enable = True, axis='x', tight =True)
	plt.show()

second_derivative()

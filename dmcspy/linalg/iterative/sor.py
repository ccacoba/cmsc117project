import numpy as np

def sor(A, b, x, tol = 1e-12, M = 50000, w = .25):
	n = len(A)
	A = np.array(A)
	b = np.array(b)
	x = np.array(x)
	it =0
	
	error = np.linalg.norm(np.dot(A,x) - b) / np.linalg.norm(b)
	while error > tol and it < M :
		it = it + 1
		x_temp = x
		for i in range(n):
			s=0
			for j in range(i):
				s = s+ A[i][j]*x[j]
			for j in range(i+1, n):
				s= s+ A[i][j]*x_temp[j]
			x_temp[i] = (b[i]-s)/A[i][i]
			x[i]= w*(b[i]-s)/A[i][i] + (1-w)*x_temp[i]
		error = np.linalg.norm(np.dot(A,x) - b) / np.linalg.norm(b)
	return x
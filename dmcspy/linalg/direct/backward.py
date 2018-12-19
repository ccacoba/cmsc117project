from time import time
def bckward(U, b):
	start = time()
	#Solves the linear system Ux=b where
	# U is a upper triangular matrix and b is a vector.
	n = len(b) 
	#initialize x	
	x = [0 for k in range(n)] 
	#list with 0 of n Components.
	x[n-1] = b[n-1]/ U[n-1][n-1]
	for j in range(n-2, -1, -1):
		x[j] = (b[j] - sum(U[j][i]*x[i] for i in range(j+1, n))) / U[j][j]
	end = time()
	return x, (end- start)
	

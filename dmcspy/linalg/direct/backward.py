def backward(U, b):
	#Solves the linear system Lx=b where
	# L is a upper triangular matrix and b is a vector.
	n = len(b) 
	#initialize x	
	x = [0 for k in range(n)] 
	#list with 0 of n Components.
	x[n-1] = b[n-1]/ L[n-1][n-1]
	for j in range(n-2, -1, -1):
		x[j] = (b[j] - sum(U[j][i]*x[i] for i in range(j+1, n))) / U[j][j]
	return x
def lu(A):
	n= len(A)
	for k in range(n-1):
		for j in range(k+1, n):
			A[j][k] = A[j][k]/A[k][k]
		for i in range(k+1, n):
			A[i][j] = A[i][j] - A[i][k]*A[k][j]

	L = [[0 for k in range(n)] for k in range(n)]	
	U = [[0 for k in range(n)] for k in range(n)]	

	for k in range(n):
		L[k][k] = 1.0

	for row in range(n):
		for col in range(n):
			if col >=	row:
				U[row][col] = A[row][col]
			else:
				L[row][col]	= A[row][col]	
	return L,U	


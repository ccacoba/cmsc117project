def forward(L, b):
	#Solves the linear system Lx=b where
	# L is a lower triangular matrix and b is a vector.
	n = len(b) 
	#initialize x
	x = [0 for k in range(n)] 
	#list with 0 of n Components.
	x[0] = b[0]/ L[0][0]
	for j in range(1, n):
		x[j] = (b[j] - sum(L[j][i]*x[i] for i in range(j))) / L[j][j]
	return x
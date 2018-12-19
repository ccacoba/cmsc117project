from time import time
def fwdward(L, b):
	start = time()
	#Solves the linear system Lx=b where
	# L is a lower triangular matrix and b is a vector.
	start = time()
	n = len(b) 
	#initialize x
	x = [0 for k in range(n)] 
	#list with 0 of n Components.
	x[0] = b[0]/ L[0][0]
	for j in range(1, n):
		x[j] = (b[j] - sum(L[j][i]*x[i] for i in range(j))) / L[j][j]
	end = time()
	runtime = end - start
	return x, runtime
	
#Low = [[2, 0, 0], [3,5,0], [7,8,9]]
#bb = [2,8,24]
#x = forward(Low, bb)
#print(x)	
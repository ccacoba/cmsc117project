def gem(A, b):
#LU factorization
	L, U = LU(A)
	newY = ForwardSub(L,b)
	newX = BackwardSub(U,y)

	return newX	
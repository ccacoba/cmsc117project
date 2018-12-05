def JOR(A,b,x,w=1000,tol=1e-10):
    error = 1
    n = A.shape[0]
    while error > tol:
        x_temp = dp(x)
        for i in range(n):
            s = 0
            for j in range(n):
                s = s + A.item((i,j))*x_temp.item((j,0))
            x[i] = (w/A.item((i,i)))*(b.item((i,0))-s)+(1-w)*x_temp.item((i,0))
            error = norm(A*x-b)/norm(b)
    return x
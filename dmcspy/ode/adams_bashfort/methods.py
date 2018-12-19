__author__ = 'Imman Narciso'
from time import time
import numpy as np

"""
This Adam's Bashforth method is under the dmcspy.odes

While the Euler, and RK methods makes use of singel step methods, or use only a one previous point to compute the next.
The Adam's Bashforth method gets two initial points x0, and x1(which solved using Euler).

Arguments:
        T           -   Final time  
        N           -   Number of steps
        function    -   function f used
        init        -   initial value x0

Output:
        x           -   coordinates of the approximated first order degree differential equation
        time        -   process time
"""
    
def adams2(T,N,function,init):
        start1 = time()
        grid = np.linspace(0, T, N+1) #generates an equally segmented grid 
        h = grid[1] - grid[0]
        size = len(init)#pre-allocation
        x = np.zeros((size, len(grid))) 
        x[:,0] = init
        for k in range(N):
                if k == 0:
                        x[:, k+1] = x[:,k]+ h*f(x[:,k])
                else:       
                        x[:,k+1] = x[:, k] +(h/2)*(3*f(x[:,k])-f(x[:,k-2]))
        end = time()
        t = end - start1
        return x, t

def adams3(T,N,function,init):
        start = time()
    	#step = finalTime/ numTimeSteps
        grid = np.linspace(0, T, N+1)
        h = grid[1] - grid[0]
        size = len(init)#pre-allocation
        x = np.zeros((size, len(grid))) 
        x[:,0] = init
        for k in range(N):
                if k == 0:
                        x[:, k+1] = x[:,k]+ h*f(x[:,k])
                else:              
                        x[:,k+1] = x[:, k] +(h/12)*(23*f(x[:,k])-16*f(x[:,k-2])+5*f(x[:,k-2]))
        end = time()
        t = end - start
        return x, t

    

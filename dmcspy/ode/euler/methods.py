__author__ = 'Imman Narciso'
from time import time
import numpy as np

"""
This method approximates a solution of first order differential equations from a given initial value.
Among the variations of this method are the ff:

                        Forward Euler
------------------------------------------------------------------
The most basic Euler method given is the forward Euler method, which
gets the previous value as basis per iteration. The forward Euler method
is based on a truncated Taylor series expansion. (web.mit.edu)


                        Backward Euler
------------------------------------------------------------------
Or called the 'Implicit Euler' 

                            Theta
------------------------------------------------------------------
The theta method is a variation of the previous methods, where theta, bounded
by [0,1],  is an example of a general approach to designing algorithms in which
geometric intuition is replaced by Taylor series expansion. Invariably the implicit
function theorem is also used in the design and analysis of scheme. (math.oregonstate.edu)

This method can also be implented as the previous methods, i.e if theta = 0 generates the
Backward euler, theta = 1/2 generates the Crank - Nicolson, etc.
------------------------------------------------------------------
Arguments:
        T           -   Final time  
        N           -   Number of steps
        function    -   function f used
        init        -   initial value x0

Output:
        x           -   coordinates of the approximated first order degree differential equation
        time        -   process time
"""
def forward(T, N, function, init):
        start = time()
        grid = np.linspace(0, T, N+1)#this initializes the total number of steps, equallt=y segmented by N
        h = grid[1] - grid[0] 
        size = len(init)#init.shape[0]
        #pre-allocation
        x = np.zeros((size, len(grid))) 
        x[:,0] = init
        for k in range(N):
        	x[:, k+1] = x[:,k]+ h*f(x[:,k])
        end = time()
        t = end -start
        return x, t

def backward( T, N ,function, init):
        start = time()
        grid = np.linspace(0, T, N+1) #generates equally segmented values of t
        h = grid[1] - grid[0]
        size = len(init)
        #pre-allocation
        x = np.zeros((size, len(grid))) 
        x[:,0] = init
        for k in range(N):
                x[:,k+1] = x[:,k] + h*f(x[:,k+1])
        end = time()
        t = end -start    
        return x, t
    
def theta(T, N ,function, init,theta = 0.5):
        start = time()
        grid = np.linspace(0, T, N+1)#this initializes the total number of steps, equallt=y segmented by N
        h = grid[1] - grid[0]
        size = len(init)
        #pre-allocation
        x = np.zeros((size, len(grid))) 
        x[:,0] = init
        for k in range(N):
        	x[:, k+1] = x[:,k]+ h*(theta*f(x[:,k]) + (1-theta)*f(x[:,k+1]))
        end = time()
        t = end -start
        return x, t
    


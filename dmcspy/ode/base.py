from .euler import *
from .adams_bashfort import *
from .rk import *
from matplotlib import pyplot as plt
"""
This method displays the graph the solutions of the First order Differential
equations by the different methods for ODEs

arguments:
        time     -    boolean value to print the time elapsed(in ms)
        x        -    displays the graph of the chosen method that's used
"""
def PrintResults(x_val, time_val, x=True, time=True):
        if x:
                plt.plot(x_val[0,:], x_val[1,:],'bs', ls = '-.', ms = '1.0')
                plt.xlabel('t')
                plt.ylabel('x(t)')
                plt.show()
        if time:
                print("Time elapsed: ", end='')
                print(time_val)

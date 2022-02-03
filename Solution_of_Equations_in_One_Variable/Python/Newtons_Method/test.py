from newtons_method import *
import numpy as np
import math

def f(x):
    return (np.cos(x)-x)

def Df(x):
    return (-np.sin(x)-1)

print(newtons_method((np.pi/4), pow(10, -5), 10, f, Df))
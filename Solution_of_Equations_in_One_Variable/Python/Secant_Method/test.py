from secant_method import *
import numpy as np
import math

def f(x):
    return (np.cos(x)-x)

print(secant_method(0.5, np.pi/4, pow(10, -7), 10, f))
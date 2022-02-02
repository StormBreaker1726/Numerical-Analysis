from bisection_method import *
import numpy as np
import math

def f(x):
    return (math.pow(x, 4) - 3 * math.pow(x, 2) - 3)

print(bisection_method(1, 2, 0.01, 18, f))
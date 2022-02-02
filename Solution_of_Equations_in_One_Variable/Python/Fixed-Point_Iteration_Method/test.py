from fixed_point_iteration import *
import numpy as np
import math

def g(p):
    return math.pow((3+3*math.pow(p,2)), 1/4)

print(fixed_point_iteration(1, 0.01, 10, g))
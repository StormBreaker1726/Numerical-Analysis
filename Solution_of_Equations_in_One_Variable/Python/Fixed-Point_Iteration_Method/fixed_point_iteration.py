import math as mt
import numpy as np

def fixed_point_iteration(p0, tol, max_it, g):
    i = 0
    while (i < max_it):
        p = g(p0)
        if(np.abs(p - p0) < tol):
            print("The procedure was successful.")
            return p
        else:
            i = i + 1
            p0 = p
    return p
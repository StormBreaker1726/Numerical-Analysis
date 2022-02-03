import math as mt
import numpy as np


def newtons_method(p0, tol, max_it, f, Df):
    i = 0
    
    while (i < max_it):
        p = p0 - (f(p0)/Df(p0))
        if(abs(p - p0) < tol):
            print("The procedure was succesful.")
            return p 
        else:
            i = i + 1
            p0 = p 
    
    print("Mathod failed after " + str(max_it) + " iterations. The procedure was unsuccessful.")
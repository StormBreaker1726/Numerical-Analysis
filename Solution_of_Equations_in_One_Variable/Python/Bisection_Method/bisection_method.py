import math as mt
import numpy as np

def bisection_method(a, b, tol, max_it, f):
    i = 0
    FA = f(a)
    
    while(i < max_it):
        p = (a)+((b-a)/2)
        FP = f(p)
        
        if(FP == 0 or (b-a)/2 < tol):
            print("The procedure was successful.")
            return p 
        else:
            i = i + 1
            if(FA * FP > 0):
                a = p
                FA = FP
            else:
                b = p
    
    print("Mathod failed after " + str(max_it) + " iterations. The procedure was unsuccessful.")
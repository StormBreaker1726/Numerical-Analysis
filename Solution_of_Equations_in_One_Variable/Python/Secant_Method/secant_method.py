import math as mt
import numpy as np

def secant_method(p0, p1, tol, max_it, f):
    i = 1
    q0 = f(p0)
    q1 = f(p1)
    
    while(i < max_it):
        p = p1 - q1*((p1 - p0)/(q1 - q0))
        
        if(abs(p - p1) < tol):
            print("The procedure was successful.")
            return p 
        
        i = i + 1
        
        p0 = p1 
        q0 = q1 
        p1 = p 
        q1 = f(p)
    print("Mathod failed after " + str(max_it) + " iterations. The procedure was unsuccessful.")
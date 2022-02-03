import math as mt
import numpy as np

#can be called Regula Falsi
def false_position_method(p0, p1, tol, max_it, f):
    i = 1
    q0 = f(p0)
    q1 = f(p1)
    
    while (i < max_it):
        p = p1 - q1*((p1 - p0) / (q1 - q0))
        
        if(abs(p - p1) < tol):
            print("The procedure was succesful.")
            return p
        
        i = i + 1
        q = f(p)
        
        if(q*q1 < 0):
            p0 = p1 
            q0 = q1 
        
        p1 = p 
        q1 = q 

    print("Mathod failed after " + str(max_it) + " iterations. The procedure was unsuccessful.")
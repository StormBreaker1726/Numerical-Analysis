import math
import numpy as np

def func(x, y):
    return (x-y)

def Euler(h, x0, y0, xf):
    x = np.arange(x0, xf + h/2, h)
    y = np.zeros(len(x))
    y[0] = y0

    tam = (len(x))

    for i in range(tam - 1):
        k = y[i] + h*func(x[i], y[i])
        y[i + 1] = y[i] + (h/2) * (func(x[i], y[i]) + func(x[i]+h, k))
    return y

h = 0.005
x0 = 1
xf = 2
y0 = 4

y = Euler(h, x0, y0, xf)

print(y[-1])

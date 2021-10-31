import math

def func(x):
    y = math.sqrt(math.pow(x,3)-1)
    return y

def regra_dos_trapezios(a, b, n):
    if n == 0:
        print("Division by zero")
    else:
        if n < 0:
            print("Invalid interval")
        else:
            h = (b - a)/n
            x = a + h
            sum = 0
            for i in range(1, n - 1):
                sum = sum + func(x)
                x = x + h
            I = h * ((func(a) + func(b))/2 + sum)
            return I

file = open("results.txt", "a")
original = 11.822489758289
j = 3
I = regra_dos_trapezios(1, 2, j)
erro = ((original-I)/original)

print("Resultado foi de " + str(I) + ", com erro de " + str(erro) + ", usando " + str(j) + " passos\n")

file.close()

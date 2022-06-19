'''
Newton-Raphson Method
'''
from math import *

def newton(f, df, x0, eps, k_max):
    k = 0
    while k < k_max:
        if (abs(f(x0)) <= eps):
            erro = f(x0)
            break
        else:
            k += 1
        x = x0 - f(x0)/df(x0)
        x0 = x
    return (x0, erro, k)


def main():
    f = lambda x: sin(x)     # Insert f(x)
    df = lambda x: cos(x)        # Insert f'(x)
    #Parameters: (f(x), f'(x), Initial x, precision, max iteractions)
    print(newton(f, df, 3.15, 10**(-10), 100))


if __name__ == '__main__':
    main()
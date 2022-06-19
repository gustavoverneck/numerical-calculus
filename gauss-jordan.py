'''
Método de Gauss-Jordan
-> Resolve sistemas de equações do tipo:
 __                           .
| a1 * x1 + a2 * x2 + a3 * x3 . k1
| b1 * x1 + b2 * x2 + b3 * x3 . k2
| c1 * x1 + c2 * x2 + c3 * x3 . k3
| ...                         .
|__                           .

Diagonaliza a matriz.
'''
from math import *
import numpy as np
from pyparsing import col

def main():
    #Square Matrix
    X = np.array([
        [+2, +3, -1, -7, +23],
        [+1, +1, +1, +4, -32],
        [-1, -2, +3, +15, -4],
        [+3, -13, -8, +1, +1]
    ])

    # Matriz inferior
    for i in range(len(X)):
        for j in range(i+1,len(X)):
            r = X[i][i] / X[j][i]
            A = X[j]
            X[j] = np.multiply(A,r) - X[i]    
    print(X)

    # Matriz Superior
    for i in range(len(X)-1, 0, -1):
        for j in range(i-1, -1, -1):
            r = X[j][i] / X[i][i]
            A = X[i]
            X[j] = np.multiply(A,r) - X[j]
    print(X)

    for i in range(len(X)):
        A = X[i]
        X[i] = np.multiply(A, 1/X[i][i])

    # Resultados
    for i in range(len(X)):
        print("X_{} = {}".format(i, X[i][len(X)]))

if __name__ == "__main__":
    main()
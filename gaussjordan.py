import numpy as np
import sys

def gaussJordan(a, b):
    n = int(len(b))
    j = 0
    for i in a: # Adds b to A for solving
        i.append(b[j])
        j += 1

    # Gauss-Jordan Elimination
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Division by zero detected!')
        
        for j in range(n):
            if i != j :
                m = a[j][i]/a[i][i]

                for k in range(n+1):
                    a[j][k] = a[j][k] - m*a[i][k]
    # output
    x = []
    for i in range(n):
        x.append(a[i][n])
    return x


if __name__ == '__main__':
    A = [
        [1, 1, 1],
        [2, -3, 4],
        [3, 4, 5]
        ]
    b = [9, 13, 40]
    x = gaussJordan(A, b)
    print(x)
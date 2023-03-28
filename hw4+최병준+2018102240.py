import utility
from numpy import *

def order(p, i ,j):

    """this"""

    if i != j:
        k = p[i][j]
        print("(", end='')
        order(p, i, k)
        order(p, k + 1, j)
        print(")", end='')

    elif i == j:
        print("A " + str(i), end='')

    """this"""

d = array([5, 2, 3, 4, 6, 7, 8])
n = len(d)-1

m = array([[0 for j in range(1, n+2)] for i in range(1, n+2)])
p = array([[0 for j in range(1, n+2)] for i in range(1, n+2)])

"""this"""

for diag in range(1, n):

    for i in range(1, n-diag+1):

        a = 1000
        b = i
        j = diag + i

        for k in range(i, j):

            num = m[i][k] + m[k+1][j] + d[i-1]*d[k]*d[j]

            if num < a:
                a = num
                b = k

        m[i][j] = a
        p[i][j] = b

"""this"""

utility.printMatrix(m)
print()
utility.printMatrix(p)
order(p, 1, 6)
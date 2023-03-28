from numpy import *

"""(1)빠른 정렬"""
def quickSort(s, low, high, c=0):
   if high > low:
       s, pivotpoint = partition(s, low, high)
       quickSort(s, low, pivotpoint-1)
       quickSort(s, pivotpoint+1, high)
   return c

def partition(s, low, high):
   pivotitem = s[low]
   i = low
   j = high
   while i<j:
       while s[i] <= pivotitem and i < high:
           i += 1
       while s[j] >= pivotitem and j > low:
           j -= 1
       if i < j:
           s[i], s[j] = s[j], s[i]
   s[low], s[j] = s[j], s[low]
   return s, j

n = 8
s = []
c = int(n * log(n))
for e in range(20):
    g = []
    for f in range(n):
        k = random.randint(0, n + 1)
        g.append(k)
    s.append(g)
for h in range(len(s)):
    quickSort(s[h], 0, len(s[h])-1)
    print(s[h])
print("평균 데이터 비교 횟수 :", c)


"""(2)쉬트라센 알고리즘"""

def strassen(n, A, B, C):
    threshold = 2
    A11 = array([[A[rows][cols] for cols in range(int(n/2))] for rows in range(int(n/2))])

    """this"""

    A12 = array([[A[rows][cols] for cols in range(int(n/2), int(n))] for rows in range(int(n/2))])
    A21 = array([[A[rows][cols] for cols in range(int(n/2))] for rows in range(int(n/2), int(n))])
    A22 = array([[A[rows][cols] for cols in range(int(n/2), int(n))] for rows in range(int(n/2), int(n))])

    B11 = array([[B[rows][cols] for cols in range(int(n/2))] for rows in range(int(n/2))])
    B12 = array([[B[rows][cols] for cols in range(int(n/2), int(n))] for rows in range(int(n/2))])
    B21 = array([[B[rows][cols] for cols in range(int(n/2))] for rows in range(int(n/2), int(n))])
    B22 = array([[B[rows][cols] for cols in range(int(n/2), int(n))] for rows in range(int(n/2), int(n))])

    """this"""

    #print(A11, A12, A21, A22, B11, B12, B21, B22)
    if(n <= threshold):
        C = array(A) @ array(B)
    else:
        M1 = M2 = M3 = M4 = M5 = M6 = M7 = array([])
        M1 = strassen(int(n/2), (A11 + A22), (B11 + B22), M1)

        """this"""

        M2 = strassen(int(n/2), (A21 + A22), B11, M2)
        M3 = strassen(int(n/2), A11, (B12 - B22), M3)
        M4 = strassen(int(n/2), A22, (B21 - B11), M4)
        M5 = strassen(int(n/2), (A11 + A12), B22, M5)
        M6 = strassen(int(n/2), (A21 - A11), (B11 + B12), M6)
        M7 = strassen(int(n/2), (A12 - A22), (B21 + B22), M7)

        """this"""

        C = vstack([hstack([M1+M4 - M5 + M7, M3 + M5]), hstack([M2 + M4, M1 + M3 - M2 + M6])])
    return C

N=4
#A = [[1 for cols in range(n)] for rows in range(n)]
#B = [[2 for cols in range(n)] for rows in range(n)]
A = [[1, 2, 0, 2], [3, 1, 0, 0], [0, 1, 1, 2], [2, 0, 2, 0]]
B = [[0, 3, 0, 2], [1, 1, 4, 0], [1, 1, 0, 2], [0, 5, 2, 0]]
C = array(A)@array(B)
D = [[0 for cols in range(N)] for rows in range(N)]
print(C)
D = strassen(N, A, B, D)
print(D)
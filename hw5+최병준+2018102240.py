import utility

# 최적 이진 검색트리
class Node:
    def __init__(self, data):
        self.l_child = None
        self.r_child = None
        self.data = data

def tree(key, r, i, j):
    k = r[i][j]
    if k == 0:
        return
    else:
        p = Node(key[k])
        p.l_child = tree(key, r, i, k-1)
        p.r_child = tree(key, r, k+1, j)
        return p

key = [" ", "A", "B", "C", "D", "E"]
p = [0, 3/15, 1/15, 2/15, 5/15, 4/15]
n = len(p)-1

a = [[0 for j in range(0, n+2)] for i in range(0, n+2)]
r = [[0 for j in range(0, n+2)] for i in range(0, n+2)]

for i in range(1, n+1):
        a[i][i-1] = 0
        a[i][i] = p[i]
        r[i][i] = i
        r[i][i-1] = 0
a[n+1][n] = 0
r[n+1][n] = 0


"""this"""

def optsearchtree(n, p, minavg, R):

    for i in range(1, n):
        for q in range(1, n - i + 1):
            m = i + q
            minN1 = float("inf")
            for k in range(q, m + 1):
                if minavg[q][k - 1] + minavg[k + 1][m] < minN1:
                    minN1 = minavg[q][k - 1] + minavg[k + 1][m]
                    minN2 = k

            sig = 0
            for z in range(q, m + 1):
                sig += p[z]

            minavg[q][m] = minN1 + sig
            R[q][m] = minN2
    return minavg, R

a, r = optsearchtree(n, p, a, r)

"""this"""

print("***최적 이진 검색트리***")

utility.printMatrixF(a)
print()
utility.printMatrix(r)

root = tree(key, r, 1, n)
utility.print_inOrder(root)
print()
utility.print_preOrder(root)

print()
print("***DNA 서열맞춤알고리즘***")

# DNA 서열맞춤알고리즘
a = ['T','G','A']
b = ['T', 'A']

m = len(a) #len(a) = 10
n = len(b) #len(b) = 8
table = [[0 for j in range(0, n+1)] for i in range(0, m+1)]
minindex = [[(0, 0) for j in range(0, n+1)] for i in range(0, m+1)]

for j in range(n-1, -1, -1):
    table[m][j] = table[m][j+1] + 2

for i in range(m-1, -1, -1):
    table[i][n] = table[i+1][n] + 2

"""this"""

def opt(i, j):
    if i == m:
        opt_val = 2 * (n - j)
    elif j == n:
        opt_val = 2 * (m - i)
    else:
        if a[i] == b[j]:
            penalty = 0
        else:
            penalty = 1
        opt_val = min(opt(i + 1, j + 1)+penalty, opt(i + 1, j) + 2, opt(i, j + 1) + 2)
    return opt_val

for j in range(n-1, -1, -1):
    for i in range(m-1, -1, -1):
        table[i][j] = opt(i, j)

def mintable(i, j):
    if table[i][j] == table[i][j + 1] + 2:
        minindex[i][j] = (i, j + 1)
        if j + 1 < n:
            mintable(i, j + 1)
    elif table[i][j] == table[i + 1][j] + 2:
        minindex[i][j] = (i + 1, j)
        if i + 1 < m:
            mintable(i + 1, j)
    else:
        minindex[i][j] = (i + 1, j + 1)
        if i + 1 < m and j + 1 < n:
            mintable(i + 1, j + 1)

mintable(0, 0)

"""this"""

utility.printMatrix(table)
x=0
y=0

while (x < m and y < n):
    tx, ty = x, y
    print(minindex[x][y])
    (x,y) = minindex[x][y]
    if x == tx + 1 and y == ty + 1:
        print(a[tx], " ", b[ty])
    elif x == tx and y == ty+1:
        print(" - ", " ", b[ty])
    else:
        print(a[tx], " ", " -")
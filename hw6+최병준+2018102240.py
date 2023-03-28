#Dijkstra 알고리즘

inf = 1000

w = [[0, 7, 4, 6, 1], [inf, 0, inf, inf, inf],
[inf, 2, 0, 5, inf], [inf, 3, inf, 0, inf], [inf, inf, inf, 1, 0]]

n = 5
f = set()
touch = n*[0]
length = n*[0]
save_length = n*[0]

"""this"""

def dijkstra(n, w, f):
    
    for i in range(n - 1):
        
        v_1 = inf
        
        for j in range(1, n):
            
            if(0 <= length[j] and length[j] < v_1):
       
                v_1 = length[j]
       
                v_2 = j
       
        V = (touch[v_2], v_2)
       
        f.add(V)
       
        for k in range(1, n):
       
            if(length[v_2] + w[v_2][k] < length[k]):
       
                length[k] = length[v_2] + w[v_2][k]
       
                touch[k] = v_2
       
        save_length[v_2] = length[v_2]
       
        length[v_2] = -1
    
    return f

for m in range(1, n):

    length[m] = w[0][m]

dijkstra(n, w, f)

print(f)

"""this"""

print(save_length)



#n-Queens 알고리즘
def promising(i, col):
    
    """this"""
    
    j = 0

    check = True

    while(j < i and check == True):

        if(col[i] == col[j] or abs(col[i] - col[j]) == i - j):
            check = False

        j += 1

    return check
    
    """this"""

def queens(n, i, col, m):

    """this"""

    global queens_count

    if promising(i, col):
        
        if i == n - 1:
            
            queens_count += 1

            if queens_count == m:

                print("{0}번째 해 : {1}".format(m, col))
        
        else :
            
            for j in range(n):
                
                col[i+1] = j
                
                queens(n, i + 1, col, m)
    
    """this"""

queens_count = 0
n = 7
col = n*[0]
m = 2
queens(n, -1, col, m)
print("해의 총개수 : ", queens_count)
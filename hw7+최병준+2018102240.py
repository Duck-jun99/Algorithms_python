#부분집합의 합
def promising(i, weight, total):
    
    """this"""
    return (weight + total >= W) and (weight == W or weight + s[i+1] <= W)
    """this"""

def s_s(i, weight, total, include):
    
    """this"""
    #sum of subsets
    if promising(i, weight, total):
        if weight == W:
            print("sol " + str(include))
        else:
            include[i + 1] = 1
            s_s(i + 1, weight + s[i + 1], total - s[i + 1], include)
            include[i + 1] = 0
            s_s(i + 1, weight, total-s[i + 1], include)
    """this"""

n = 6
s = [1, 2, 3, 4, 5, 6]
W = 11
print("items =", s, "W =", W)
include = n*[0]
total = 0

for k in s:
    total +=k
s_s(-1, 0, total, include)

#m-coloring

def color(i, vcolor):

    """this"""
    if promising(i, vcolor):
        if(i == n - 1):
            print(vcolor)
        else:
            for k in range(1, m + 1):
                vcolor[i + 1] = k
                color(i + 1, vcolor)
    """this"""

def promising(i, vcolor):

    """this"""
    k = 1
    switch = True

    while k < i and switch:
        if W[i][k] and vcolor[i] == vcolor[k]:
            switch = False
        k += 1

    return switch
    """this"""

n = 5
W = [[0,1,1,1,1],[1,0,1,0,1],[1,1,0,1,0],[1,0,1,0,1],[1,0,1,1,0]]
vcolor = n*[0]
m = 3
color(-1, vcolor)
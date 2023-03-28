# partition 방법 (퀵정렬과 유사)
def selection(low, high, k):
    pivotpoint = -1 # 사용 전에 미리 변수를 만들어놓기
    if low == high:
        return s[low]
    else:
        pivotpoint = partition(low, high, pivotpoint)
        if k == pivotpoint:
            return s[pivotpoint]
        elif k < pivotpoint:
            return selection(low, pivotpoint-1, k)
        else:
            return selection(pivotpoint+1, high, k)

def partition(low,high,pivotpoint):
    pivotitem = s[low]
    j = low
    for i in range(low+1, high+1):
        if s[i] < pivotitem:
            j += 1
            s[i], s[j] = s[j], s[i]
    pivotpoint = j
    s[low], s[pivotpoint] = s[pivotpoint], s[low]
    return pivotpoint
    
s = [20,10,5,8,15,30,60,25]
n = len(s)
print(selection(0,n-1,1))
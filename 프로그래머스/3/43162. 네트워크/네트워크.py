def find(x, parent):
    if x == parent[x]:
        return x
    
    parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)
    
    if x == y:
        return
    
    parent[x] = y

def solution(n, computers):
    
    parent = [i for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                union(i, j, parent)
    
    for i in range(n):
        find(i, parent)
    answer = len(set(parent))
                
    return answer
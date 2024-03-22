from collections import deque

def solution(maps):
    
    inf = 999999
    n, m = len(maps), len(maps[0])
    dist = [[inf for _ in range(m)] for _ in range(n)]
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    q = deque([(0, 0, 0)])
    dist[0][0] = 0
    
    while q:
        cx, cy, cost = q.popleft()
        
        if cost > dist[cx][cy]:
            continue
        
        for nx, ny in d:
            nx += cx
            ny += cy
            if(0 <= nx < n) and (0 <= ny < m) and maps[nx][ny]:
                if cost + 1 < dist[nx][ny]:
                    q.append((nx, ny, cost + 1))
                    dist[nx][ny] = cost + 1
    

    
    if dist[n-1][m-1] == inf:
        return -1
    else:
        return dist[n-1][m-1] + 1
    
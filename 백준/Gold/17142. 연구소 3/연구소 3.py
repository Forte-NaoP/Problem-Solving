import sys
from collections import deque

INF = 1e9
diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n, m = map(int, input().split())

row = col = range(n)
lab = [list(map(int, input().split())) for _ in row]
virus = [(i, j) for i in row for j in col if lab[i][j] == 2]
act_virus = [[0, 0] for _ in range(m)]
dist = [[INF for _ in col] for _ in row]
visit = [[False for _ in col] for _ in row]
q = deque()

ans = INF

def init():
    for i in row:
        for j in col:
            dist[i][j] = INF

def bfs():
    global ans

    init()
    for vx, vy in act_virus:
        q.append((vx, vy, 0))
        dist[vx][vy] = 0

    while q:
        vx, vy, t = q.popleft()

        for dx, dy in diff:
            nx, ny = vx + dx, vy + dy

            if nx in row and ny in col and lab[nx][ny] != 1:
                if dist[nx][ny] > t + 1:
                    dist[nx][ny] = t + 1
                    q.append((nx, ny, t + 1))
    local_max = 0
    for i in row:
        for j in col:
            if lab[i][j] == 1:
                continue
            if dist[i][j] == INF and lab[i][j] != 2:
                return
            if dist[i][j] > local_max and lab[i][j] != 2:
                local_max = dist[i][j]

    if ans > local_max:
        ans = min(ans, local_max)

def track(last, cnt):
    global m
    if cnt == m:
        bfs()
        return
    
    for i in range(last + 1, len(virus)):
        act_virus[cnt][0] = virus[i][0]
        act_virus[cnt][1] = virus[i][1]
        track(i, cnt + 1)

track(-1, 0)
if ans == INF:
    ans = -1
print(ans)

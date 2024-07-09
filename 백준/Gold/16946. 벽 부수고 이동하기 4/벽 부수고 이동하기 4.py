import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
row, col = range(n), range(m)
graph = [list(map(int, list(input().strip()))) for _ in row]
visited = [[0 for _ in col] for _ in row]
diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]
q = deque()

def bfs(x, y, idx):
    visited[x][y] = idx
    q.append((x, y))
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in diff:
            nx, ny = x + dx, y + dy
            if nx not in row or ny not in col:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                visited[nx][ny] = idx
                q.append((nx, ny))
                cnt += 1
    return cnt

idx = 1
group = [0]
for i in row:
    for j in col:
        if visited[i][j] == 0 and graph[i][j] == 0:
            cnt = bfs(i, j, idx)
            group.append(cnt)
            idx += 1

for i in row:
    for j in col:
        cnt = 0
        chk = []
        if graph[i][j] == 1:
            for dx, dy in diff:
                x, y = i + dx, j + dy
                if x not in row or y not in col:
                    continue
                if visited[x][y] not in chk:
                    cnt += group[visited[x][y]]
                    chk.append(visited[x][y])
            graph[i][j] = (cnt + 1) % 10

for i in row:
    print(''.join(map(str, graph[i])))
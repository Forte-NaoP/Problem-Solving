import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
pool = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
for i in range(1, n + 1):
    pool[i][1:-1] = list(map(int, list(input().strip())))[:]
row = range(1, n + 1)
col = range(1, m + 1)

diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visit = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
def bfs(x, y, idx):
    q = deque([(x, y)])
    min_wall = 10
    first_height = pool[x][y]
    flood = [(x, y)]
    visit[x][y] = idx

    while q:
        x, y = q.popleft()

        for dx, dy in diff:
            nx, ny = x + dx, y + dy
            if nx not in row or ny not in col:
                return 0
            if pool[nx][ny] <= first_height and visit[nx][ny] != idx:
                q.append((nx, ny))
                flood.append((nx, ny))
                visit[nx][ny] = idx
            elif pool[nx][ny] > first_height:
                min_wall = min(min_wall, pool[nx][ny])

    cap = 0
    for x, y in flood:
        cap += max(min_wall - pool[x][y], 0)
        pool[x][y] = min_wall
    return cap

ans = 0
idx = 1
for i in row:
    for j in col:
        if visit[i][j] == idx:
            continue
        ans += bfs(i, j, idx)
        idx += 1

print(ans)
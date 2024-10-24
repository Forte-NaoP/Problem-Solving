import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]
dist = [[99999 for _ in range(m)] for _ in range(n)]
diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]

q = deque([(0, 0, 0)])
dist[0][0] = 0
while q:
    d, x, y = q.popleft()

    for dx, dy in diff:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < n) or not (0 <= ny < m):
            continue
        if d + maze[nx][ny] >= dist[nx][ny]:
            continue
        dist[nx][ny] = d + maze[nx][ny]
        if maze[nx][ny] == 0:
            q.appendleft((dist[nx][ny], nx, ny))
        else:
            q.append((dist[nx][ny], nx, ny))

print(dist[n - 1][m - 1])
from collections import deque

diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]

n, m = map(int, input().split())
row, col = range(n), range(m)
graph = [input().strip() for _ in row]
visit = [[[False, 0] for _ in col] for _ in row]
q = deque([(0, 0, 1, 0)])
visit[0][0][0] = True
ans = 123456789
while q:
    x, y, d, b = q.popleft()

    if x == n - 1 and y == m - 1:
        ans = min(ans, d)
        continue

    for dx, dy in diff:
        nx, ny = x + dx, y + dy
        if nx not in row or ny not in col:
            continue

        if graph[nx][ny] == '1' and b == 0:
            q.append((nx, ny, d + 1, 1))
            visit[nx][ny][1] = True
        elif graph[nx][ny] == '0' and not visit[nx][ny][b]:
            q.append((nx, ny, d + 1, b))
            visit[nx][ny][b] = True

print(ans if ans != 123456789 else -1)
import sys

input = lambda : sys.stdin.readline().strip()

INF = 10 ** 9
n, m = map(int, input().split())
dist = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = 0
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if dist[i][j] != INF or dist[j][i] != INF:
            cnt += 1
    if cnt == n - 1:
        ans += 1

print(ans)
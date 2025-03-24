import sys

input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
graph = [[10 ** 9 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1][v - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] != 10 ** 9 and graph[j][i] != 10 ** 9:
            print(-1)
            exit(0)

ans = []
for i in range(n):
    l, r = 0, n - 1
    for j in range(n):
        if graph[i][j] != 10 ** 9:
            r -= 1
        elif graph[j][i] != 10 ** 9:
            l += 1
    ans.append(f'{l + 1} {r + 1}')
    
print('\n'.join(ans))
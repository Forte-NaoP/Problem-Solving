import sys
from collections import deque, defaultdict

n, m = map(int, input().split())
row, col = range(n), range(m)
sea = [list(map(int, input().split())) for _ in range(n)]
visit = [[False for _ in range(m)] for _ in range(n)]
diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]

island_num = 2
island = defaultdict(list)
graph = defaultdict(dict)

q = deque()
def bfs(x, y, island_num):
    q.append((x, y))
    sea[x][y] = island_num
    island[island_num].append((x, y))

    while q:
        x, y = q.popleft()
        for dx, dy in diff:
            nx, ny = x + dx, y + dy
            if nx in row and ny in col and sea[nx][ny] == 1:
                q.append((nx, ny))
                sea[nx][ny] = island_num
                island[island_num].append((nx, ny))
    
for i in range(n):
    for j in range(m):
        if sea[i][j] == 1:
            bfs(i, j, island_num)
            island_num += 1

for k in island.keys():
    for x, y in island[k]:
        for dx, dy in diff:
            nx, ny = x + dx, y + dy
            while nx in row and ny in col and sea[nx][ny] == k:
                nx, ny = nx + dx, ny + dy
            if nx not in row or ny not in col:
                continue

            dist = 0
            while nx in row and ny in col and sea[nx][ny] == 0:
                nx, ny = nx + dx, ny + dy
                dist += 1
            if nx not in row or ny not in col or dist < 2:
                continue
            
            if graph[k].get(sea[nx][ny]) is None:
                graph[k][sea[nx][ny]] = dist
            else:
                graph[k][sea[nx][ny]] = min(graph[k][sea[nx][ny]], dist)

if len(island.keys()) != len(graph.keys()):
    print(-1)
    exit()

parent = [i for i in range(island_num)]
edge = []

def find(x):
    if parent[x] == x:
        return parent[x]

    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    parent[x] = y

for k in graph.keys():
    for nxt, cost in graph[k].items():
        edge.append((cost, k, nxt))

ans, cnt = 0, island_num - 3
edge = sorted(edge, reverse=True)

while cnt:
    if not edge:
        print(-1)
        exit()
    cost, a, b = edge.pop()
    if find(a) != find(b):
        union(a, b)
        ans += cost
        cnt -= 1

print(ans)

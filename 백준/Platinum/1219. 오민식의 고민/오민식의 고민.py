import sys
from collections import deque, defaultdict

input = sys.stdin.readline

edge = []
g = defaultdict(list)
n, s, e, m = map(int, input().split())
for _ in range(m):
    edge.append(list(map(int, input().split())))
    g[edge[-1][0]].append(edge[-1][1])

city = list(map(int, input().split()))
for i in range(m):
    b = edge[i][1]
    edge[i][2] = city[b] - edge[i][2]

def bfs(st, ed, n):
    q = deque([st])
    visit =  [False for _ in range(n + 1)]
    visit[st] = True

    while q:
        cur = q.popleft()
        if cur == ed:
            return True
        
        for nxt in g[cur]:
            if visit[nxt]:
                continue
            q.append(nxt)
            visit[nxt] = True

    return False

def bf(st, ed, val, n):
    dist = [-sys.maxsize for _ in range(n + 1)]
    dist[st] = val
    for i in range(n):
        for a, b, c in edge:
            if dist[a] != -sys.maxsize and dist[b] < dist[a] + c:
                dist[b] = dist[a] + c 
                if i == n - 1:
                    if bfs(b, ed, n):
                        return 'Gee'
    return dist[ed] if dist[ed] != -sys.maxsize else 'gg'

print(bf(s, e, city[s], n))

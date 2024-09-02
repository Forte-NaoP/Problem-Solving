import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = defaultdict(lambda : defaultdict(lambda : 1e9))
for _ in range(n):
    line = list(map(int, input().split()))
    cur = line[0]
    for i in range(1, len(line) - 1, 2):
        nxt, cost = line[i], line[i + 1]
        graph[cur][nxt] = cost

visit = [0 for _ in range(n + 1)]
dist = [0 for _ in range(n + 1)]
rx, rd = 0, 0

def dfs(cur, idx):
    global rx, rd
    for nxt, cost in graph[cur].items():
        if visit[nxt] == idx:
            continue
        visit[nxt] = idx
        dist[nxt] = cost + dist[cur]
        if dist[nxt] > rd:
            rx, rd = nxt, dist[nxt]
        dfs(nxt, idx)

visit[1] = 1
dfs(1, 1)
visit[rx], dist[rx] = 2, 0
dfs(rx, 2)
print(rd)
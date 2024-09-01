import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())
parent = [-1 for _ in range(1001)]
dp = [[-1 for _ in range(1001)] for _ in range(1001)]

def init(x):
    for i in range(1, x + 1):
        for j in range(1, x + 1):
            dp[i][j] = -1

def dfs(x, p):
    parent[x] = p
    for nxt in graph[x].keys():
        if nxt == p:
            continue
        dfs(nxt, x)

def recur(x):
    if len(graph[x]) == 1 and x != 1:
        return 20001
    
    ret = 0
    for nxt in graph[x].keys():
        if nxt == parent[x]:
            continue
        dp[x][nxt] = min(graph[x][nxt], recur(nxt))
        ret += dp[x][nxt]
    return ret

for _ in range(t):
    n, m = map(int, input().split())
    graph = defaultdict(dict)
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c
    dfs(1, -1)
    print(recur(1))
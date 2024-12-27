import sys
from typing import List, Deque
from collections import deque

input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    c, *nxt = map(int, input().split())
    g[i].extend(nxt)

INF = 10 ** 9
def hopcroft_karp(g, n, m):
    pair_U = [-1] * (n + 1)  # U의 매칭
    pair_V = [-1] * (m + 1)  # V의 매칭
    
    # 레벨 배열
    dist = [-1] * (n + 1)

    def bfs():
        queue = deque()
        for u in range(1, n + 1):
            if pair_U[u] == -1:  # 매칭되지 않은 U 노드
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF

        while queue:
            u = queue.popleft()
            for v in g[u]:
                nxt_u = pair_V[v]
                if nxt_u != -1 and dist[nxt_u] == INF:
                    dist[nxt_u] = dist[u] + 1
                    queue.append(nxt_u)

    def dfs(u):
        for v in g[u]:
            nxt_u = pair_V[v]
            if nxt_u == -1 or dist[nxt_u] == dist[u] + 1 and dfs(nxt_u):
                pair_U[u] = v
                pair_V[v] = u
                return True
        return False

    matching = 0
    while True:
        bfs()
        find = 0
        for u in range(1, n + 1):
            if pair_U[u] == -1 and dfs(u):
                find += 1
        if find == 0:
            break
        matching += find

    return matching, pair_U, pair_V

print(hopcroft_karp(g, n, m)[0])

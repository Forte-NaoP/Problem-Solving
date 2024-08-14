import sys
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop

input = sys.stdin.readline
n, e = map(int, input().split())
graph = defaultdict(list)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())
INF = 999_999_999

def dijkstra(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    q = []
    hpush(q, (0, start))
    while q:
        cost, cur = hpop(q)
        for nxt, n_cost in graph[cur]:
            if dist[nxt] > cost + n_cost:
                dist[nxt] = cost + n_cost
                hpush(q, (dist[nxt], nxt))
    return dist

dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

if (dist[v1] == INF or dist[v2] == INF) or (v1_dist[n] == INF or v2_dist[n] == INF):
    print(-1)
else:
    answer = min(dist[v1] + v1_dist[v2] + v2_dist[n], dist[v2] + v2_dist[v1] + v1_dist[n])
    print(answer)
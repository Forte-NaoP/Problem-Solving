import sys
import heapq

input = sys.stdin.readline
hpush = heapq.heappush
hpop = heapq.heappop

v, e = map(int, input().split())
k = int(input())

graph = [dict() for _ in range(20001)]

for _ in range(e):
    _u, _v, _w = map(int, input().split())
    if graph[_u].get(_v) is None: 
        graph[_u][_v] = _w
    else:
        graph[_u][_v] = min(graph[_u][_v], _w)

INF = 99999999
dist = [INF] * 20001

dist[k] = 0
pq = [(0, k)]

while (pq):
    cost, cur = hpop(pq)
    for nxt_node, nxt_cost in graph[cur].items():
        nxt_cost += cost
        if (dist[nxt_node] < nxt_cost):
            continue
        dist[nxt_node] = nxt_cost
        hpush(pq, (nxt_cost, nxt_node))

for i in range(1, v + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
import sys
import heapq

hpush = heapq.heappush
hpop = heapq.heappop

INF = 1e9

n, d = map(int, input().split())
graph = {}
for i in range(10001):
    graph[i] = {}
    graph[i][i + 1] = 1

dist = [INF for _ in range(10001)]

for _ in range(n):
    s, t, c = map(int, input().split())
    if c >= t - s:
        continue
    if graph[s].get(t) is None:
        graph[s][t] = c
    graph[s][t] = min(graph[s][t], c)

def dijkstra(st):
    global d
    for i in range(10001):
        dist[i] = INF

    dist[st] = 0
    pq = [(0, st)]

    while pq:
        cost, cur = hpop(pq)

        if dist[cur] < cost or graph.get(cur) is None:
            continue
        
        for nxt, nx_cost in graph[cur].items():
            if nxt > d:
                continue
            if dist[nxt] > cost + nx_cost:
                dist[nxt] = cost + nx_cost
                hpush(pq, (cost + nx_cost, nxt))

dijkstra(0)
print(dist[d])
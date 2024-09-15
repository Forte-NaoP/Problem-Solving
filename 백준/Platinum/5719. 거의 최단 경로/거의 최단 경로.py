import sys
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

def dijkstra(g, route, dist, s):
    pq = [(s, 0)]
    dist[s] = 0

    while pq:
        cur, cost = hpop(pq)
        if dist[cur] < cost:
            continue

        for nxt, nxt_cost in g[cur].items():
            if nxt_cost == -1:
                continue
            nxt_cost += cost
            if nxt_cost < dist[nxt]:
                dist[nxt] = nxt_cost
                route[nxt].clear()
                route[nxt].append(cur)
                hpush(pq, (nxt, nxt_cost))
            elif nxt_cost == dist[nxt]:
                route[nxt].append(cur)

route = [deque() for _ in range(501)]
dist = [sys.maxsize for _ in range(501)]

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    s, e = map(int, input().split())

    for i in range(501):
        dist[i] = sys.maxsize
        route[i].clear()

    graph = defaultdict(dict)
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c

    dijkstra(graph, route, dist, s)

    q = deque()
    for before in route[e]:
        q.append((before, e))

    while q:
        cur, nxt = q.popleft()
        graph[cur][nxt] = -1
        while route[cur]:
            before = route[cur].popleft()
            q.append((before, cur))

    for i in range(501):
        dist[i] = sys.maxsize

    dijkstra(graph, route, dist, s)

    print(dist[e] if dist[e] != sys.maxsize else - 1)
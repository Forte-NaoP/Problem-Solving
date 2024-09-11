import sys
from collections import defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

n, m = map(int, input().split())

cross = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    cross[a].append((i, b))
    cross[b].append((i, a))

dist = [sys.maxsize for _ in range(n + 1)]

def dijkstra(start):
    global n, m
    pq = []
    hpush(pq, (0, start))
    dist[start] = 0

    while pq:
        cost, cur = hpop(pq)
        if cost > dist[cur]:
            continue
        
        for timing, nxt in cross[cur]:
            period = (cost - timing) // m
            if (cost - timing) % m != 0:
                period += 1
            nxt_cost = timing + period * m + 1
            if dist[nxt] > nxt_cost:
                dist[nxt] = nxt_cost
                hpush(pq, (nxt_cost, nxt))

dijkstra(1)
print(dist[n])
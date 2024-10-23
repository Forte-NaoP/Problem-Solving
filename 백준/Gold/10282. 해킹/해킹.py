import sys
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

def dijkstra(g, n, c):
    dist = [10 ** 9 for _ in range(n + 1)]
    dist[c] = 0
    pq = [(0, c)]
    cnt, time = 0, 0
    while pq:
        cost, cur = hpop(pq)
        if cost > dist[cur]:
            continue
        time = max(time, cost)
        cnt += 1
        for nxt, nxt_cost in g[cur]:
            nxt_cost += cost
            if nxt_cost < dist[nxt]:
                dist[nxt] = nxt_cost
                hpush(pq, (nxt_cost, nxt)) 
    return cnt, time

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    print(*dijkstra(graph, n, c))

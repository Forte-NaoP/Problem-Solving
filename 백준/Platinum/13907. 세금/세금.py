import sys
from collections import defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

n, m, k = map(int, input().split())
start, end = map(int, input().split())
graph = defaultdict(lambda: defaultdict(lambda: 10 ** 9))
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])
    graph[b][a] = graph[a][b]

dist = [[10 ** 9 for _ in range(n + 1)] for _ in range(n + 1)]

def dijkstra(st):
    pq = []
    hpush(pq, (0, st, 0))
    dist[st][0] = 0

    while pq:
        d, cur, cnt = hpop(pq)
        if min(dist[cur][:cnt + 1]) < d:
            continue
        for nxt in graph[cur].keys():
            nxt_d = graph[cur][nxt]
            if d + nxt_d < dist[nxt][cnt + 1]:
                dist[nxt][cnt + 1] = d + nxt_d
                hpush(pq, (d + nxt_d, nxt, cnt + 1))

dijkstra(start)
print(min(dist[end]))
for _ in range(k):
    t = int(input())
    for i in range(1, n + 1):
        dist[end][i] += i * t
    print(min(dist[end]))

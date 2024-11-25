import sys
from itertools import permutations
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
INF = float('inf')

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

st, ed = map(int, input().split())
p = int(input())
mid = list(map(int, input().split()))

def dijkstra(st, n):
    dist = [INF for _ in range(n + 1)]
    pq = [(0, st)]
    dist[st] = 0

    while pq:
        cur_d, cur = hpop(pq)
        if cur_d > dist[cur]:
            continue
        for nxt, nxt_d in g[cur]:
            nxt_d += cur_d
            if nxt_d < dist[nxt]:
                dist[nxt] = nxt_d
                hpush(pq, (nxt_d, nxt))
    
    return dist

dist = dict()
for p in mid:
    dist[p] = dijkstra(p, n)
dist[st] = dijkstra(st, n)

ans = INF
for p1, p2, p3 in permutations(mid, 3):
    tmp = dist[st][p1] + dist[p1][p2] + dist[p2][p3] + dist[p3][ed]
    if tmp < ans:
        ans = tmp
if ans == INF:
    ans = -1
print(ans)
import sys
from collections import defaultdict
from itertools import combinations, permutations
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
hrp = heapq.heapreplace
heapify = heapq.heapify

input = lambda : sys.stdin.readline().strip()

n, m, k = map(int, input().split())
g = [[] for _ in range(n + 1)]
INF = float('inf')

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))

dist = [[] for _ in range(n + 1)]

def kth_dijkstra():
    hpush(dist[1], 0)
    pq = [(0, 1)]

    while pq:
        cur_d, cur = hpop(pq)

        for nxt, nxt_d in g[cur]:
            nxt_d += cur_d
            if len(dist[nxt]) < k:
                hpush(dist[nxt], -nxt_d)
                hpush(pq, (nxt_d, nxt))
            else:
                if dist[nxt][0] < -nxt_d:
                    hrp(dist[nxt], -nxt_d)
                    hpush(pq, (nxt_d, nxt))

kth_dijkstra()
ans = []
for i in range(1, n + 1):
    if len(dist[i]) < k:
        ans.append(-1)
    else:
        ans.append(-dist[i][0])

print('\n'.join(map(str, ans)))
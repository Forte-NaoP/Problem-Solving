import sys
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = lambda : sys.stdin.readline().strip()

op = [lambda x: x >> 1, lambda x: x << 1]
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c << 1))
    g[b].append((a, c << 1))

INF = sys.maxsize
distA = [INF for _ in range(n + 1)]
distB = [[INF, INF] for _ in range(n + 1)]

pq = [(0, 1)]
distA[1] = 0
while pq:
    dA, cA = hpop(pq)
    if distA[cA] < dA:
        continue
    for nxt, nxt_dist in g[cA]:
        nxt_dist += dA
        if nxt_dist < distA[nxt]:
            distA[nxt] = nxt_dist
            hpush(pq, (nxt_dist, nxt))

pq = [(0, 1, 1)]
while pq:
    dB, cB, o = hpop(pq) 
    if distB[cB][o] < dB:
        continue
    o ^= 1
    for nxt, nxt_dist in g[cB]:
        nxt_dist = op[o](nxt_dist) + dB
        if nxt_dist < distB[nxt][o]:
            distB[nxt][o] = nxt_dist
            hpush(pq, (nxt_dist, nxt, o))

iter = zip(distA, distB)
next(iter)
ans = -1
for a, b in iter:
    if a < min(b):
        ans += 1
print(ans)

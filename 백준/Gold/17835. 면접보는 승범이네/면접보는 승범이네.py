import sys
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

n, m, k = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, c = map(int, input().split())
    g[v].append((u, c))

point = list(map(int, input().split()))
dist = [float('inf') for _ in range(n + 1)]
dist[0] = 0
pq = []
for p in point:
    pq.append((0, p))
    dist[p] = 0

while pq:
    cost, cur = hpop(pq)

    if cost > dist[cur]:
        continue

    for nxt, nxt_cost in g[cur]:
        nxt_cost += cost
        if nxt_cost >= dist[nxt]:
            continue
        hpush(pq, (nxt_cost, nxt))
        dist[nxt] = nxt_cost

max_num, max_dist = 0, -1
for i in range(1, n + 1):
    if dist[i] > max_dist:
        max_num = i
        max_dist = dist[i]
    elif dist[i] == max_dist:
        max_num = min(i, max_num)

print(f'{max_num}\n{max_dist}')

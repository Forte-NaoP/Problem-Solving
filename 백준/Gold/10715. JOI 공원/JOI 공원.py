import sys
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = lambda : sys.stdin.readline().strip()

n, m, c = map(int, input().split())
g = [dict() for _ in range(n + 1)]
dist = [float('inf') for _ in range(n + 1)]
parent = [[] for _ in range(n + 1)]
connect = [False for _ in range(n + 1)]
total_road = 0
max_road = 0
for _ in range(m):
    a, b, d = map(int, input().split())
    max_road = max(max_road, d)
    total_road += d
    g[a][b] = d
    g[b][a] = d

# dijkstra(1)
dist[1] = 0
pq = [(0, 1)]
while pq:
    d, cur = hpop(pq)
    for nxt, nxt_dist in g[cur].items():
        nxt_dist += d
        if dist[nxt] > nxt_dist:
            hpush(pq, (nxt_dist, nxt))
            dist[nxt] = nxt_dist
            parent[nxt] = [cur]
        elif dist[nxt] == nxt_dist:
            parent[nxt].append(cur)
# dijkstra end

dist = sorted(enumerate(dist[1:], start=1), key=lambda x: x[1])
connect[1] = True
repair_cost = total_road
left_road = total_road
idx = 1
while idx < n:
    cur, x = dist[idx]
    connect[cur] = True
    for nxt, nxt_dist in g[cur].items():
        if connect[nxt]:
            left_road -= nxt_dist
    repair_cost = min(repair_cost, c * x + left_road)
    idx += 1
print(repair_cost)
import sys
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = lambda : sys.stdin.readline().strip()

n, m, k = map(int, input().split())
g = [[] for _ in range(n + 1)]
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
    edges.append((c, a, b))
edges.sort()

def dijkstra(n, k, limit):
    dist = [float('inf') for _ in range(n + 1)]
    pq = [(0, 1)]
    dist[1] = 0

    while pq:
        cur_dist, cur = hpop(pq)

        if dist[cur] > cur_dist:
            continue

        for nxt, nxt_dist in g[cur]:
            nxt_dist = cur_dist + (nxt_dist > limit)
            if nxt_dist < dist[nxt]:
                dist[nxt] = nxt_dist
                hpush(pq, (nxt_dist, nxt))

    return dist[n] <= k

ans = -1
low, high = 0, 1_000_000
while low <= high:
    mid = (low + high) // 2
    if dijkstra(n, k, mid):
        high = mid - 1 
        ans = mid        
    else:
        low = mid + 1

print(ans)
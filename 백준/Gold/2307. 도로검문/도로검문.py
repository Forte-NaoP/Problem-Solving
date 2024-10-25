import sys
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

n, m = map(int, input().split())
road = defaultdict(dict)
for _ in range(m):
    a, b, c = map(int, input().split())
    road[a][b] = c
    road[b][a] = c

trace = [[] for _ in range(n + 1)]
def dijkstra(first):
    dist = [10 ** 9 for _ in range(n + 1)]
    pq = [(0, 1)]
    dist[1] = 0

    while pq:
        cost, cur = hpop(pq)

        for nxt, nxt_cost in road[cur].items():
            nxt_cost += cost
            if nxt_cost < dist[nxt]:
                if first:
                    trace[nxt] = [cur]
                dist[nxt] = nxt_cost
                hpush(pq, (nxt_cost, nxt))
            elif nxt_cost == dist[nxt]:
                if first:
                    trace[nxt].append(cur)
    
    return dist[n]

init_val = dijkstra(True)
candidate = []
q = deque([n])
while q:
    cur = q.popleft()
    for p in trace[cur]:
        candidate.append((cur, p, road[cur][p]))
        q.append(p)

ans = 0
for a, b, c in candidate:
    road[a][b] = road[b][a] = 10 ** 9
    val = dijkstra(False)
    if val == 10 ** 9:
        ans = -1
        break
    ans = max(ans, val - init_val)
    road[a][b] = road[b][a] = c

print(ans)
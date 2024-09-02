import sys
from collections import defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

v, e = map(int, input().split())
graph = defaultdict(lambda : defaultdict(lambda : 1e9))
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = graph[b][a] = min(graph[a][b], c)

node_cnt = 0
nodes = [False for _ in range(v + 1)]
mst_weight = 0

pq = []
for nxt, weight in graph[1].items():
    hpush(pq, (weight, nxt))
nodes[1] = True

while node_cnt < v and pq:
    weight, cur = hpop(pq)
    if nodes[cur]:
        continue

    mst_weight += weight
    nodes[cur] = True
    node_cnt += 1

    for nxt, weight in graph[cur].items():
        if not nodes[nxt]:
            hpush(pq, (weight, nxt))

print(mst_weight)

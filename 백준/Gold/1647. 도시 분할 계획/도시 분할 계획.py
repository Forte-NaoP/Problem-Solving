import sys
from copy import deepcopy
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop

input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(lambda: 1_000_000_000)

for _ in range(m):
    a, b, c = map(int, input().split())
    if a > b:
        a, b = b, a
    graph[(a, b)] = min(graph[(a, b)], c)

edges = list(map(lambda x: (x[1], *x[0]), graph.items()))
edges.sort()

parent = [[i, 1] for i in range(n + 1)]

def find(x):
    if parent[x][0] == x:
        return x
    parent[x][0] = find(parent[x][0])
    return parent[x][0]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    parent[a][0] = b
    parent[b][1] += parent[a][1]
    return True

cost = 0

for c, a, b in edges:
    if union(a, b):
        cost += c
        if parent[find(a)][1] == n:
            cost -= c
            break

print(cost)
import sys
from copy import deepcopy
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop

input = sys.stdin.readline

v, e = map(int, input().split())
edge = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))

edge.sort()

parent = [i for i in range(v + 1)]

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[a] = b

weight = 0
for c, a, b in edge:
    if find(a) != find(b):
        union(a, b)
        weight += c
print(weight)
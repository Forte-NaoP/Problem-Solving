import sys
from copy import deepcopy
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)
indegree = [0] * (n + 1)
parent = [i for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append((i, i))
q.sort()
group = defaultdict(deque)

heapify(q)
pq = []

while q:
    cur, root = hpop(q)
    group[root].append(cur)

    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            hpush(q, (nxt, root))

for key in list(group.keys()):
    hpush(pq, (group[key].popleft(), key))
    if not group[key]:
        del group[key]

ans = []
while pq:
    cur, root = hpop(pq)
    ans.append(str(cur))
    if group[root]:
        hpush(pq, (group[root].popleft(), root))
        if not group[root]:
            del group[root]

print(' '.join(ans))
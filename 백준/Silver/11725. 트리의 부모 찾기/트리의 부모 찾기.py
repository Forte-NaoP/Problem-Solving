import sys
from collections import deque

n = int(input())
tree = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque()
q.append(1)

while q:
    cur = q.popleft()
    for nxt in tree[cur]:
        if parent[nxt] == 0:
            parent[nxt] = cur
            q.append(nxt)

for i in range(2, n + 1):
    print(parent[i])

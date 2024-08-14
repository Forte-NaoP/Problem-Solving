import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

v1 = [False] * (n + 1)
v2 = [False] * (n + 1)
d1 = [0] * (n + 1)
d2 = [0] * (n + 1)

def dfs(start, visit, dist):
    q = deque()
    q.append(start)
    visit[start] = True
    while q:
        cur = q.popleft()
        for nxt, cost in tree[cur]:
            if not visit[nxt]:
                visit[nxt] = True
                dist[nxt] = dist[cur] + cost
                q.append(nxt)
    return max(dist), dist.index(max(dist))

l1, e1 = dfs(1, v1, d1)
l2, e2 = dfs(e1, v2, d2)

print(l2)
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
parent = [-1 for _ in range(n + 1)]
dp = [[0, 0] for _ in range(n + 1)]
dq = [[]]
max_depth = 0

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque([(1, 0, -1)])

while q:
    cur, depth, p = q.popleft()
    if len(dq) <= depth:
        dq.append([])
    dq[depth].append(cur)
    max_depth = max(max_depth, depth)

    for nxt in tree[cur]:
        if nxt == p:
            continue
        q.append((nxt, depth + 1, cur))
        parent[nxt] = cur


while max_depth >= 0 and dq[max_depth]:
    cur = dq[max_depth].pop()

    dp[cur][0] += 1
    p = parent[cur]

    dp[p][1] += dp[cur][0]
    dp[p][0] += min(dp[cur])
    
    if not dq[max_depth]:
        max_depth -= 1

print(min(dp[1]))

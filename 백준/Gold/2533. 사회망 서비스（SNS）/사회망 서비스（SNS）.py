import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
visit = [False for _ in range(n + 1)]
parent = [-1 for _ in range(n + 1)]
dp = [[0, 0] for _ in range(n + 1)]
dq = [[] for _ in range(n + 1)]
max_depth = 0

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque([(1, 0)])
visit[1] = True

while q:
    cur, depth = q.popleft()
    dq[depth].append(cur)
    max_depth = max(max_depth, depth)

    for nxt in tree[cur]:
        if not visit[nxt]:
            q.append((nxt, depth + 1))
            parent[nxt] = cur
            visit[nxt] = True


while max_depth >= 0 and dq[max_depth]:
    cur = dq[max_depth].pop()

    dp[cur][0] += 1
    p = parent[cur]

    dp[p][1] += dp[cur][0]
    dp[p][0] += min(dp[cur])
    
    if not dq[max_depth]:
        max_depth -= 1

print(min(dp[1]))

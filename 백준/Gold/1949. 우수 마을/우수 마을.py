import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
cp = [0] + list(map(int, input().split()))
conn = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    conn[a].append(b)
    conn[b].append(a)

dp = [[0, 0] for _ in range(n + 1)]

def dfs(cur, p):
    if len(conn[cur]) == 1 and conn[cur][0] == p:
        dp[cur][0] = cp[cur]
        return
    
    dp[cur][0] = cp[cur]
    for nxt in conn[cur]:
        if nxt == p:
            continue
        dfs(nxt, cur)
        dp[cur][1] += max(dp[nxt])
        dp[cur][0] += dp[nxt][1]
    return

dfs(1, 0)
print(max(dp[1]))
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
visit = [False for _ in range(n + 1)]
dp = [[0, 0] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(x):
    visit[x] = True
    dp[x][0] = 1

    for nxt in tree[x]:
        if not visit[nxt]:
            dfs(nxt)
            dp[x][1] += dp[nxt][0]
            dp[x][0] += min(dp[nxt])

dfs(1)
print(min(dp[1]))
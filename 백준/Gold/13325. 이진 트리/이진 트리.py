import sys
input = sys.stdin.readline

n = 2 ** (int(input()) + 1)
edge = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n)]

# dp[x]: node x부터 leaf까지의 거리
def dfs(x):
    if x * 2 >= n:
        return 0
    if dp[x] != 0:
        return dp[x]
    dp[x] = max(dfs(x * 2) + edge[x * 2 - 1], dfs(x * 2 + 1) + edge[x * 2])
    return dp[x]

dfs(1)
ans = 0
for i in range(2, n):
    ans += dp[i // 2] - dp[i]
print(ans)
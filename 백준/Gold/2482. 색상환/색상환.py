import sys
input = sys.stdin.readline

n, k = int(input()), int(input())
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
MOD = 1_000_000_003

for i in range(n + 1):
    dp[i][1] = i
    dp[i][0] = 1

for i in range(2, n + 1):
    for j in range(2, k + 1):
        dp[i][j] = dp[i - 2][j - 1] + dp[i - 1][j] % MOD

print((dp[n - 3][k - 1] + dp[n - 1][k]) % MOD)
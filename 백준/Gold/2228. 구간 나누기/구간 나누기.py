import sys
input = sys.stdin.readline

n, m = map(int, input().split())
prefix = [0]
for _ in range(n):
    prefix.append(prefix[-1] + int(input()))

dp = [[-1e9 for _ in range(m + 1)] for _ in range(n + 1)]
dp[1][1] = prefix[1]

for i in range(2, n + 1):
    dp[i][1] = dp[i - 1][1]
    for j in range(i):
        dp[i][1] = max(dp[i][1], prefix[i] - prefix[j])

for i in range(3, n + 1):
    for j in range(2, m + 1):
        dp[i][j] = dp[i - 1][j]
        for k in range(1, i - 1):
            dp[i][j] = max(dp[i][j], dp[k][j - 1] + prefix[i] - prefix[k + 1])

print(dp[n][m])  
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
male = list(map(int, input().split()))
female = list(map(int, input().split()))

male.sort()
female.sort()

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j - 1] + abs(male[i - 1] - female[j - 1])
        if i > j:
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
        elif i < j:
            dp[i][j] = min(dp[i][j], dp[i][j - 1])

print(dp[n][m])
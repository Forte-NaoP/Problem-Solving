import sys

input = sys.stdin.readline

w, h = map(int, input().split())
dp = [[[[0, 0], [0, 0]] for _ in range(w)] for _ in range(h)]

for j in range(w):
    dp[0][j][0][1] = 1

for i in range(h):
    dp[i][0][0][0] = 1

for i in range(1, h):
    for j in range(1, w):
        dp[i][j][0][1] = dp[i][j - 1][0][1] + dp[i][j - 1][1][1]
        dp[i][j][1][1] = dp[i][j - 1][0][0]
        dp[i][j][0][0] = dp[i - 1][j][0][0] + dp[i - 1][j][1][0]
        dp[i][j][1][0] = dp[i - 1][j][0][1]

print(sum(map(sum, dp[h - 1][w - 1])) % 100000)
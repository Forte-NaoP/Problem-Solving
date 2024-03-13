import sys

input = sys.stdin.readline

n, k = map(int, input().split())
w, v = [0] * 101, [0] * 101
dp = [[0 for _ in range(100_001)] for _ in range(101)]

goods = []
for i in range(1, n + 1):
    w[i], v[i] = map(int, input().split())

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j < w[i] : 
            dp[i][j] = dp[i - 1][j]
        else :
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])

print(dp[n][k])


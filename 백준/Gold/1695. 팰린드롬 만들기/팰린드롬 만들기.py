import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

dp = [[0 for _ in range(n + 1)] for _ in range(2)]

for i in reversed(range(n)):
    for j in range(i + 1, n):
        row = i % 2
        if seq[i] != seq[j]:
            dp[row][j] = min(dp[row - 1][j], dp[row][j - 1]) + 1
        else:
            dp[row][j] = dp[row - 1][j - 1]

print(dp[0][n - 1])
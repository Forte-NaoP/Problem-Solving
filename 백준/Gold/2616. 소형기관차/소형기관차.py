import sys
input = sys.stdin.readline

n = int(input())
train = [0] + list(map(int, input().split()))
prefix = [0]
for i in range(1, n + 1):
    prefix.append(prefix[-1] + train[i])
m = int(input())
dp = [[0 for _ in range(n + 1)] for _ in range(4)]

for i in range(1, 4):
    for j in range(i * m, n + 1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - m] + prefix[j] - prefix[j - m])

print(dp[3][n])

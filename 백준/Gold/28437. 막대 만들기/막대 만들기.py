import sys

input = sys.stdin.readline

dp = [0 for _ in range(100_001)]
n, stick = int(input()), list(map(int, input().split()))
q, target = int(input()), list(map(int, input().split()))

for a in stick:
    dp[a] += 1

for i in range(1, 100_001):
    for j in range(i * 2, 100_001, i):
        dp[j] += dp[i]

for t in target:
    print(dp[t], end=' ')
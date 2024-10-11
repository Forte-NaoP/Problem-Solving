import sys

input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
for i in range(1, n):
    seq[i] += seq[i - 1]

ans = [0 for _ in range(n)]
if seq[-1] % 4 != 0:
    print(0)
else:
    dp = [1, 0, 0, 0]
    target = seq[-1] // 4
    for i in range(n - 1):
        for j in range(3, 0, -1):
            if seq[i] == target * j:
                dp[j] += dp[j - 1]
    print(dp[3])
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
jewel = [int(input()) for _ in range(n)]
acc = [jewel[0]]
for i in range(1, n):
    acc.append(acc[-1] + jewel[i]) 

# dp[i]: i번째 보석부터 연속해서 m개 이상 집었을때 최댓값
dp = [0 for _ in range(n)]
dp[n - m] = acc[-1] - acc[n - m - 1]
for i in range(n - m - 1, -1, -1):
    if dp[i + 1] >= acc[i + m - 1] - acc[i]:
        dp[i] = dp[i + 1]
    else:
        dp[i] = acc[i + m - 1] - acc[i]
    dp[i] += jewel[i]

print(max(dp))
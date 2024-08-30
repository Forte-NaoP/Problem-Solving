import sys
input = sys.stdin.readline

n, m = map(int, input().split())
usage = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
total_cost = sum(cost)
min_cost = sys.maxsize

dp = [[0 for _ in range(total_cost + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(total_cost + 1):
        if j - cost[i] < 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - cost[i]] + usage[i], dp[i - 1][j])

        if dp[i][j] >= m:
            min_cost = min(min_cost, j)
            
print(min_cost)

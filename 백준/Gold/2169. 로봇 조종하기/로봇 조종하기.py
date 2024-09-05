import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
row, col = range(n), range(m)
mars = [list(map(int, input().split())) for _ in row]
dp = [[-sys.maxsize for _ in col] for _ in row]

dp[0][0] = mars[0][0]
for j in range(1, m):
    dp[0][j] = dp[0][j - 1] + mars[0][j]

lr = [0 for _ in col]
rl = [0 for _ in col]

for i in range(1, n):
    lr[0] = dp[i - 1][0] + mars[i][0]
    for k in range(1, m):
        lr[k] = max(dp[i - 1][k], lr[k - 1]) + mars[i][k]
    
    rl[-1] = dp[i - 1][-1] + mars[i][-1]
    for k in range(m - 2, -1, -1):
        rl[k] = max(dp[i - 1][k], rl[k + 1]) + mars[i][k]
    
    for j in range(m):
        dp[i][j] = max(lr[j], rl[j])

print(dp[-1][-1])

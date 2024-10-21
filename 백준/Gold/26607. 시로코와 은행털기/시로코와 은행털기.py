import sys

input = sys.stdin.readline

dp = [[False for _ in range(80 * 200 + 1)] for _ in range(81)]

n, k, x = map(int, input().split())
stat = [list(map(int, input().split())) for _ in range(n)]
for a, b in stat:
    for i in range(k - 1, -1, -1):
        for j in range(x * k, a - 1, -1):
            dp[i + 1][j] |= dp[i][j - a]
    dp[1][a] = True

ans = 0
for i in range(x * k + 1):
    if dp[k][i]:
        ans = max(ans, i * (x * k - i))
print(ans)

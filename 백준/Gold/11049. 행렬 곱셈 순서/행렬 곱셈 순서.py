import sys
input = sys.stdin.readline

n = int(input())
row, col = [1], [1]
for _ in range(n):
    r, c = map(int, input().split())
    row.append(r)
    col.append(c)

dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for j in range(1, n):
    for i in range(1, n - j + 1):
        dp[i][i + j] = sys.maxsize
        for w in range(i, i + j):
            dp[i][i + j] = min(dp[i][i + j], dp[i][w] + dp[w + 1][i + j] + row[i] * col[w] * col[i + j])

print(dp[1][n])

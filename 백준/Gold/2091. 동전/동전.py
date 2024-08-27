import sys
input = sys.stdin.readline

n, *coin = map(int, input().split())
value = [1, 5, 10, 25]

dp = [[-1, -1, -1, -1, -1] for _ in range(n + 1)]
dp[0] = [0, 0, 0, 0, 0]

for i in range(1, n + 1):
    for j in range(4):
        before = i - value[j]
        if before < 0:
            continue
        if dp[before][4] > dp[i][4] and coin[j] > dp[before][j]:
            dp[i][4] = dp[before][4] + 1
            dp[i][:4] = dp[before][:4]
            dp[i][j] += 1

if all(i == -1 for i in dp[n][:4]):
    print(0, 0, 0, 0)
else:
    print(*dp[n][:4])
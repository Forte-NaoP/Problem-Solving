import sys
from copy import deepcopy
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop

input = sys.stdin.readline

# dp[x][y][z] = 끝 수가 z이고 y의 켜진 비트의 인덱스를 포함하고 있는 길이 x 인 계단수의 갯수 (0 <= k < 1024)
MOD = 1_000_000_000

n = int(input())

dp = [[[0 for _ in range(10)] for _ in range(1024)] for _ in range(101)]
for i in range(1, 10):
    dp[1][1 << i][i] = 1

for i in range(2, n + 1):
    for j in range(1024):
        for k in range(1, 9):
            dp[i][j | 1 << (k - 1)][k - 1] += dp[i - 1][j][k]
            dp[i][j | 1 << (k + 1)][k + 1] += dp[i - 1][j][k]
        dp[i][j | 1 << 1][1] += dp[i - 1][j][0]
        dp[i][j | 1 << 8][8] += dp[i - 1][j][9]

ans = 0
for k in range(10):
    ans = (ans + dp[n][1023][k]) % MOD
print(ans)
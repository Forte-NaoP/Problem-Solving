import sys
from copy import deepcopy
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

n, k = map(int, input().split())
score = list(map(int, input().split()))
cost = list(map(int, input().split()))

dp = [[0 for _ in range(101)] for _ in range(n + 1)]
dp[0][100] = 0

for i in range(n):
    for j in range(101):
        if j - cost[i] >= 0:
            hp = min(j - cost[i] + k, 100)
            dp[i + 1][hp] = max(dp[i + 1][hp], dp[i][j] + score[i])
        hp = min(j + k, 100)
        dp[i + 1][hp] = max(dp[i + 1][hp], dp[i][j])
        
print(max(dp[n]))
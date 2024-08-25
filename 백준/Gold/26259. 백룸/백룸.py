import sys
from copy import deepcopy
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())
dp = [[-1e9 for _ in range(m)] for _ in range(n)]
dp[0][0] = room[0][0]

if x1 > x2:
    x1, x2 = x2, x1
if y1 > y2:
    y1, y2 = y2, y1

def wall(x, y, d):
    if d == 0:
        return x1 == x2 and x1 == x and y1 <= y < y2
    else:
        return y1 == y2 and y1 == y and x1 <= x < x2
    
for i in range(n):
    for j in range(m):
        if dp[i][j] == -1e9:
            continue
        if i < n - 1 and not wall(i + 1, j, 0):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + room[i + 1][j])
        if j < m - 1 and not wall(i, j + 1, 1):
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + room[i][j + 1])

if dp[n - 1][m - 1] != -1e9:
    print(dp[n - 1][m - 1])
else:
    print('Entity')
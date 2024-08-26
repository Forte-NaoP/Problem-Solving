import sys
from copy import deepcopy
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

str_a = [''] + list(input().strip())
str_b = [''] + list(input().strip())
len_a, len_b = len(str_a), len(str_b)
dp = [[0 for _ in range(len_a)] for _ in range(len_b)]

for i in range(len_a):
    dp[0][i] = i
for i in range(len_b):
    dp[i][0] = i

for b in range(1, len_b):
    for a in range(1, len_a):
        if str_a[a] == str_b[b]:
            dp[b][a] = dp[b - 1][a - 1]
        else:
            dp[b][a] = min(dp[b - 1][a], dp[b - 1][a - 1], dp[b][a - 1]) + 1

print(dp[len_b - 1][len_a - 1])
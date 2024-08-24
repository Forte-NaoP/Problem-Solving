import sys
from copy import deepcopy
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

apart = [[i for i in range(1, 16)]] + [[0 for _ in range(15)] for _ in range(14)]
for i in range(1, 15):
    apart[i][0] = 1
for i in range(1, 15):
    for j in range(1, 15):
        apart[i][j] = apart[i][j - 1] + apart[i - 1][j]

t = int(input())
for _ in range(t):
    k, n = int(input()), int(input())
    print(apart[k][n - 1])

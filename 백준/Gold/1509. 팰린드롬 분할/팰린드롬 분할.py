import sys
from copy import deepcopy
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop

input = sys.stdin.readline

s = list(input().strip())
n = len(s)
div = [2501 for _ in range(n)]
is_p = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    is_p[i][i] = True
    if i < n - 1 and s[i] == s[i + 1]:
        is_p[i][i + 1] = True

for j in range(2, n):
    for i in range(j - 1):
        if s[i] == s[j] and is_p[i + 1][j - 1]:
            is_p[i][j] = True

for j in range(n):
    for i in range(j + 1):
        if not is_p[i][j]:
            continue
        if i == 0:
            div[j] = 1
        else:
            div[j] = min(div[j], div[i - 1] + 1)

print(div[n - 1])
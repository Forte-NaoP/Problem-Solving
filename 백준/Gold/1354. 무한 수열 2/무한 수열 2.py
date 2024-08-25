import sys
from copy import deepcopy
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

n, p, q, x, y = map(int, input().split())

seq = {0: 1}
def recur(t):
    if t <= 0:
        return 1
    if t in seq:
        return seq[t]
    seq[t] = recur(t // p - x) + recur(t // q - y)
    return seq[t]

recur(n)
print(seq[n])

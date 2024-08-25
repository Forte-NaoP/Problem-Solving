import sys
from copy import deepcopy
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

n, p, q = map(int, input().split())

seq = {0: 1}
def recur(x):
    if x in seq:
        return seq[x]
    
    seq[x] = recur(x // p) + recur(x // q)
    return seq[x]

recur(n)
print(seq[n])
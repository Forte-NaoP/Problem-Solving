import sys
from copy import deepcopy
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

n = int(input())
fibo = [0, 1, 1] + [0] * 50

def calc(x):
    if fibo[x] != 0:
        return fibo[x]
    fibo[x] = calc(x - 1) + calc(x - 2)
    return fibo[x]

print(calc(n))
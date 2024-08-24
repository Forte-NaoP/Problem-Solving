import sys
from copy import deepcopy
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

fibo = [0, 1, 1] + [0] * 500

def calc(x):
    if fibo[x] != 0:
        return fibo[x]
    fibo[x] = calc(x - 1) + calc(x - 2)
    return fibo[x]

while (x := int(input())) != -1:
    print(f'Hour {x}: {calc(x)} cow(s) affected')
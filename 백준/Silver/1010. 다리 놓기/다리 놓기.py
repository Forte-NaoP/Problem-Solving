import sys
from copy import deepcopy
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

fact = [1]
for i in range(1, 31):
    fact.append(fact[-1] * i)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(int(fact[m] / (fact[m - n] * fact[n])))

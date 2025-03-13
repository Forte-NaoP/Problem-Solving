import sys
from typing import List, Deque, Dict
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
hrp = heapq.heapreplace
heapify = heapq.heapify

input = lambda : sys.stdin.readline().strip()

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

if (pow(x2 - x1, 2) + pow(y2 - y1, 2) < pow(r1 + r2, 2)) :
    print('YES')
else:
    print('NO')

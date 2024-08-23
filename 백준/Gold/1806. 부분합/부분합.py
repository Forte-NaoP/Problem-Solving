import sys
from copy import deepcopy
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop

input = sys.stdin.readline

n, s = map(int, input().split())
seq = list(map(int, input().split()))
l, r = 0, 0
partail_sum = 0
ans = 1e9
while l <= r:
    if partail_sum >= s:
        ans = min(ans, r - l)        
        partail_sum -= seq[l]
        l += 1
    else:
        if r == n:
            break
        partail_sum += seq[r]
        r += 1

if ans == 1e9:
    ans = 0
print(ans)
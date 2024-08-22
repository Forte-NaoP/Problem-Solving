import sys
from copy import deepcopy
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop

input = sys.stdin.readline

n = int(input())

prime = []
is_prime = [False, False] + [True] * n
for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False

for i in range(2, n + 1):
    if is_prime[i]:
        prime.append(i)

st, ed = 0, 0 # [st, ed)
ans = 0
num = 0

while st <= ed:
    if num <= n:
        if num == n:
            ans += 1
        if ed == len(prime):
            break
        num += prime[ed]
        ed += 1
    else:
        num -= prime[st]
        st += 1

print(ans)
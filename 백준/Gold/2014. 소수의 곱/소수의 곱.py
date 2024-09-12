import sys
from copy import deepcopy
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

k, n = map(int, input().split())
prime = list(map(int, input().split()))
chk = set(prime)
pq = deepcopy(prime)
heapify(pq)
n_max = max(prime)

cnt = 0
while True:
    nth = hpop(pq)
    cnt += 1
    if cnt == n:
        print(nth)
        break
    for p in prime:
        xp = nth * p
        if (len(pq) > n and xp > n_max) or xp in chk:
            continue
        hpush(pq, xp)
        chk.add(xp)
        n_max = max(n_max, xp)
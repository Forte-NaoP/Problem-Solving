import sys
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
hrp = heapq.heapreplace
heapify = heapq.heapify

input = lambda : sys.stdin.readline().strip()

n = int(input())
man = []
for _ in range(n):
    h, o = map(int, input().split())
    man.append((min(h, o), max(h, o)))
man.sort(key=lambda x: x[1])
d = int(input())
can = []
ans = 0
for h, o in man:
    start, end = o - d, o
    if start <= h and o <= end:
        hpush(can, (h, o))
    while can:
        if not (start <= can[0][0] and can[0][1] <= end):
            hpop(can)
        else:
            break
    ans = max(ans, len(can))
print(ans)


import sys
import heapq

input = sys.stdin.readline

hpush = heapq.heappush
hpop = heapq.heappop
hpp = heapq.heappushpop
hpy = heapq.heapify

n, k = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(n)]
hpy(jewels)
bags = [int(input()) for _ in range(k)]
bags.sort()
tmp = []
ans = 0
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        hpush(tmp, -hpop(jewels)[1])
    if tmp:
        ans -= hpop(tmp)

print(ans)
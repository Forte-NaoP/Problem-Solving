import sys

input = lambda : sys.stdin.readline().strip()

from bisect import bisect_left

INF = 10 ** 10
n = int(input())
seq = list(map(int, input().split()))
lis = [INF for _ in range(n)]
end = 0

for num in seq:
    idx = bisect_left(lis, num, 0, end)
    if idx == end:
        lis[end] = num
        end += 1
    else:
        lis[idx] = num

print(end)
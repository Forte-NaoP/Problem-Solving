import sys
input = lambda : sys.stdin.readline().strip()

from bisect import bisect_left

INF = 10 ** 9

n = int(input())
seq = list(map(int, input().split()))
find_min = [INF for _ in range(n)]
end = 0

for i, num in enumerate(seq):
    idx = bisect_left(find_min, num, 0, end)
    if idx == end:
        find_min[end] = num
        end += 1
    else:
        find_min[idx] = num
        
print(end)
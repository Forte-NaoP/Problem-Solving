import sys
from itertools import islice

input = sys.stdin.readline

n, max_cap = map(int, input().split())
m = int(input())

info = []
for _ in range(m):
    a, b, c = map(int, input().split())
    info.append((a, b, c))
info.sort(key=lambda x: (x[1], x[0]))

ans = 0
truck = [max_cap for _ in range(n + 1)]

for a, b, c in info:
    box = min(min(islice(truck, a, b)), c)
    truck[a:b] = map(lambda x: x - box, islice(truck, a, b))
    ans += box

print(ans)
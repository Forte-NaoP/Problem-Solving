import sys
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v, e = map(int, input().split())
edge = []
for _ in range(e):
    a, b, c = map(int, input().split())
    hpush(edge, (c, a, b))

parent = [i for i in range(v + 1)]
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    parent[x] = y
    return True

ans = 0
while edge:
    c, a, b = hpop(edge)
    if union(a, b):
        ans += c
print(ans)
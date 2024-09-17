import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
ad = map(int, input().split())
q = deque()
ans = []

for i in range(2 * m - 1):
    nxt = next(ad)
    while q and q[-1][0] < nxt:
        q.pop()
    q.append((nxt, i))

ans.append(q[0][0])
for i in range(2 * m - 1, n):
    nxt = next(ad)
    while q and q[-1][0] < nxt:
        q.pop()
    while q and q[0][1] <= i - 2 * m + 1:
        q.popleft() 
    q.append((nxt, i))
    ans.append(q[0][0])

print(*ans)
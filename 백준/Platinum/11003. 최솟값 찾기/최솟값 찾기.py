import sys
from collections import deque

input = sys.stdin.readline

n, d = map(int, input().split())
arr = map(int, input().split())
q = deque()
for i in range(n):
    val = next(arr)
    if not q:
        q.append((i, val))
    else:
        s = max(0, i - d + 1)
        while q and q[0][0] < s:
            q.popleft()
        while q and q[-1][1] >= val:
            q.pop()
        q.append((i, val))
    print(q[0][1], end=' ')


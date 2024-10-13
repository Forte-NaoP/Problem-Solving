import sys
from collections import deque

input = sys.stdin.readline

n, d = map(int, input().split())
arr = list(map(int, input().split()))
q = deque()
for i in range(n):
    while q and q[0][0] < i - d:
        q.popleft()
    if q:
        arr[i] = max(arr[i] + q[0][1], arr[i])
    while q and q[-1][1] < arr[i]:
        q.pop()
    q.append((i, arr[i]))
print(max(arr))

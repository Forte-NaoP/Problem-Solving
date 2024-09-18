import sys
from collections import deque

input = sys.stdin.readline

size = 17

class SegTree:
    def __init__(self):
        self.base = 1 << size
        self.tree = [0 for _ in range(self.base << 1)]

    def update(self, idx, val):
        idx += self.base
        while idx > 0:
            self.tree[idx] += val
            idx >>= 1

    def query(self, mid):
        return self.__query(mid, 1, 0, self.base - 1)

    def __query(self, val, idx, l, r):
        if l == r:
            return l
        mid = (l + r) // 2
        if self.tree[idx * 2] >= val:
            return self.__query(val, idx * 2, l, mid)
        else:
            return self.__query(val - self.tree[idx * 2], idx * 2 + 1, mid + 1, r)

tree = SegTree()
n, m = map(int, input().split())
q = deque()
while len(q) < m:
    q.append(int(input()))
    tree.update(q[-1], 1)

ans = 0
ans += tree.query((m + 1) // 2)

for i in range(1, n - m + 1):
    tree.update(q.popleft(), -1)
    q.append(int(input()))
    tree.update(q[-1], 1)
    mid = tree.query((m + 1) // 2)
    ans += mid

print(ans)
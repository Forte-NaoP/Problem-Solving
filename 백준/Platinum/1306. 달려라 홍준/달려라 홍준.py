import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
ad = map(int, input().split())

class SegTree:
    def __init__(self, n) -> None:
        self.base = 1
        while n > 0:
            self.base <<= 1
            n >>= 1
        self.n = self.base * 2
        self.tree = [0 for _ in range(self.n)]

    def update(self, idx, val):
        idx += self.base
        self.tree[idx] = val
        idx >>= 1
        while idx > 0:
            self.tree[idx] = max(self.tree[idx << 1], self.tree[idx << 1 | 1])
            idx >>= 1

    def query(self, l, r, idx, s, e):
        if r < s or e < l:
            return 0
        if l <= s and e <= r:
            return self.tree[idx]
        mid = (s + e) // 2
        return max(self.query(l, r, idx << 1, s, mid), self.query(l, r, idx << 1 | 1, mid + 1, e))

tree = SegTree(n)
for i in range(n):
    nxt = next(ad)
    tree.update(i, nxt)

for i in range(m - 1, n - m + 1):
    print(tree.query(i - m + 1, i + m - 1, 1, 0, tree.base - 1), end=' ')

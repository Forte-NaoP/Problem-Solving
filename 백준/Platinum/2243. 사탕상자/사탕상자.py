import sys

input = sys.stdin.readline

class SegTree:
    def __init__(self):
        self.base = 1 << 20
        self.size = self.base * 2
        self.tree = [0 for _ in range(self.size)]

    def update(self, idx, diff):
        idx += self.base
        while idx > 0:
            self.tree[idx] += diff
            idx >>= 1
    
    def query(self, s, e, idx, val):
        if s == e:
            return s
        mid = (s + e) // 2
        if self.tree[idx * 2] >= val:
            return self.query(s, mid, idx * 2, val)
        return self.query(mid + 1, e, idx * 2 + 1, val - self.tree[idx * 2])

tree = SegTree()
n = int(input())
for _ in range(n):
    a, *b = map(int, input().split())
    if a == 2:
        tree.update(*b)
    else:
        idx = tree.query(0, tree.base - 1, 1, *b)
        print(idx)
        tree.update(idx, -1)

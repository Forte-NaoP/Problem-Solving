import sys

input = lambda : sys.stdin.readline().strip()

class SegTree:
    def __init__(self, arr):
        n = len(arr)
        self.base = 1
        while n > 0:
            self.base <<= 1
            n >>= 1
        self.n = self.base * 2
        self.t = [0 for _ in range(self.n)]

        for i in range(len(arr)):
            self.__update(i, arr[i])
    
    def __update(self, idx, val):
        idx += self.base
        val = val - self.t[idx]
        while idx > 0:
            self.t[idx] += val
            idx >>= 1

    def update(self, idx, val):
        self.__update(idx, val)

    def query(self, l, r):
        return self._query(l, r, 0, self.base - 1, 1)

    def _query(self, l, r, s, e, idx):
        if r < s or l > e:
            return 0

        if l <= s and e <= r: 
            return self.t[idx]
        
        mid = (s + e) // 2
        return self._query(l, r, s, mid, idx * 2) + self._query(l, r, mid + 1, e, idx * 2 + 1)
    
n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
segtree = SegTree(arr)
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        segtree.update(b - 1, c)
    else:
        print(segtree.query(b - 1, c - 1))

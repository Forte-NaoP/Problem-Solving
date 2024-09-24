import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

class SegTree:
    def __init__(self, arr):
        n = len(arr)
        self.base = 1
        while n > 0:
            self.base <<= 1
            n >>= 1
        self.n = self.base * 2
        self.t = [0 for _ in range(self.n)]
        self.l = [0 for _ in range(self.n)]

        for i in range(len(arr)):
            self.init(i, arr[i])
    
    def init(self, idx, val):
        idx += self.base
        while idx > 0:
            self.t[idx] += val
            idx >>= 1

    def propagation(self, s, e, idx):
        if self.l[idx] != 0:
            self.t[idx] += self.l[idx] * (e - s + 1)
            if s != e:
                self.l[idx * 2] += self.l[idx]
                self.l[idx * 2 + 1] += self.l[idx]
            self.l[idx] = 0

    def update_range(self, l, r, val):
        self._update_range(l, r, val, 0, self.base - 1, 1)

    def _update_range(self, l, r, val, s, e, idx):
        self.propagation(s, e, idx)
        if r < s or l > e:
            return
        
        if l <= s and e <= r:
            self.t[idx] += val * (e - s + 1)
            if s != e:
                self.l[idx * 2] += val
                self.l[idx * 2 + 1] += val
            return
    
        mid = (s + e) // 2
        self._update_range(l, r, val, s, mid, idx * 2)
        self._update_range(l, r, val, mid + 1, e, idx * 2 + 1)
        self.t[idx] = self.t[idx * 2] + self.t[idx * 2 + 1]

    def query(self, l, r):
        return self._query(l, r, 0, self.base - 1, 1)

    def _query(self, l, r, s, e, idx):
        self.propagation(s, e, idx)
        if r < s or l > e:
            return 0

        if l <= s and e <= r: 
            return self.t[idx]
        
        mid = (s + e) // 2
        return self._query(l, r, s, mid, idx * 2) + self._query(l, r, mid + 1, e, idx * 2 + 1)
    
n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

tree = SegTree(arr)
for _ in range(m + k):
    q, *p = map(int, input().split())
    if q == 1:
        b, c, d = p
        tree.update_range(b - 1, c - 1, d)
    else:
        b, c = p
        print(tree.query(b - 1, c - 1))
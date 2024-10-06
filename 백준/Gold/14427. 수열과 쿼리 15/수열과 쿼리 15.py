import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

class SegTree:
    def __init__(self, arr):
        n = len(arr)
        self.base = 1
        while n > 0:
            self.base <<= 1
            n >>= 1
        self.t = [[i, 10 ** 10] for i in range(self.base * 2)]
        for i in range(len(arr)):
            self.update(i, arr[i])
    
    def update(self, idx, val):
        idx += self.base
        self.t[idx][1] = val
        self.t[idx][0] = idx - self.base
        idx >>= 1
        while idx > 0:
            if self.t[idx * 2][1] > self.t[idx * 2 + 1][1]:
                self.t[idx][:] = self.t[idx * 2 + 1][:]
            else:
                self.t[idx][:] = self.t[idx * 2][:]
            idx >>= 1

    def query(self, l, r):
        return self._query(l, r, 0, self.base - 1, 1)
    
    def _query(self, l, r, s, e, idx):
        if r < s or e < l:
            return -1, 10 ** 10
        
        if l <= s and e <= r:
            return self.t[idx][0], self.t[idx][1]

        mid = (s + e) // 2
        li, lv = self._query(l, r, s, mid, idx * 2)
        ri, rv = self._query(l, r, mid + 1, e, idx * 2 + 1)
        if lv <= rv:
            return li, lv
        else:
            return ri, rv
        
n = int(input())
arr = list(map(int, input().split()))
tree = SegTree(arr)

for _ in range(int(input())):
    q, *p = map(int, input().split())
    if q == 1:
        tree.update(p[0] - 1, p[1])

    else:
        print(tree.query(0, tree.base - 1)[0] + 1)

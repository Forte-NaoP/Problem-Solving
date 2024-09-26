import sys

input = sys.stdin.readline

class SegTree:
    def __init__(self, n):
        self.base = 1
        while n > 0:
            self.base <<= 1
            n >>= 1
        self.n = self.base * 2
        self.t = [0 for _ in range(self.n + 1)]
        self.l = [0 for _ in range(self.n + 1)]

    def __propagate(self, s, e, idx):
        if self.l[idx] != 0:
            self.t[idx] += (e - s + 1) * self.l[idx]
            if s != e:
                self.l[idx * 2] += self.l[idx]
                self.l[idx * 2 + 1] += self.l[idx]
            self.l[idx] = 0

    def update_range(self, l, r, val):
        self.__update_range(l, r, val, 0, self.base - 1, 1)

    def __update_range(self, l, r, val, s, e, idx):
        self.__propagate(s, e, idx)
        
        if r < s or e < l:
            return

        if l <= s and e <= r:
            self.t[idx] += (e - s + 1) * val
            if s != e:
                self.l[idx * 2] += val
                self.l[idx * 2 + 1] += val
            return

        mid = (s + e) // 2
        self.__update_range(l, r, val, s, mid, idx * 2)
        self.__update_range(l, r, val, mid + 1, e, idx * 2 + 1)
        self.t[idx] = self.t[idx * 2] + self.t[idx * 2 + 1]

    def query(self, l, r):
        return self.__query(l, r, 0, self.base - 1, 1)
    
    def __query(self, l, r, s, e, idx):
        self.__propagate(s, e, idx)

        if r < s or e < l:
            return 0

        if l <= s and e <= r:
            return self.t[idx]
        
        mid = (s + e) // 2
        return self.__query(l, r, s, mid, idx * 2) + self.__query(l, r, mid + 1, e, idx * 2 + 1)

tree = SegTree(10 ** 5 + 1)
for _ in range(int(input())):
    l, r = map(int, input().split())
    lq, rq = tree.query(l, l), tree.query(r, r)
    
    print(lq + rq)
    if lq > 0:
        tree.update_range(l, l, -lq)
    if rq > 0:
        tree.update_range(r, r, -rq)

    l, r = l + 1, r - 1
    if l <= r:
        tree.update_range(l, r, 1)

import sys

input = sys.stdin.readline

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
            self.t[idx] ^= val
            idx >>= 1

    def propagation(self, s, e, idx):
        if self.l[idx] != 0:
            self.t[idx] ^= self.l[idx] * ((e - s + 1) % 2)
            if s != e:
                self.l[idx * 2] ^= self.l[idx]
                self.l[idx * 2 + 1] ^= self.l[idx]
            self.l[idx] = 0

    def update_range(self, l, r, val):
        self.__update_range(l, r, val, 0, self.base - 1, 1)

    def __update_range(self, l, r, val, s, e, idx):
        self.propagation(s, e, idx)
        if r < s or l > e:
            return
        
        if l <= s and e <= r:
            self.t[idx] ^= val * ((e - s + 1) % 2)
            if s != e:
                self.l[idx * 2] ^= val
                self.l[idx * 2 + 1] ^= val
            return
    
        mid = (s + e) // 2
        self.__update_range(l, r, val, s, mid, idx * 2)
        self.__update_range(l, r, val, mid + 1, e, idx * 2 + 1)
        self.t[idx] = self.t[idx * 2] ^ self.t[idx * 2 + 1]

    def query(self, x):
        return self.__query(x, x, 0, self.base - 1, 1)

    def __query(self, l, r, s, e, idx):
        self.propagation(s, e, idx)
        if r < s or l > e:
            return 0

        if l <= s and e <= r: 
            return self.t[idx]
        
        mid = (s + e) // 2
        return self.__query(l, r, s, mid, idx * 2) ^ self.__query(l, r, mid + 1, e, idx * 2 + 1)
    

n = int(input())
arr = list(map(int, input().split()))
tree = SegTree(arr)
for _ in range(int(input())):
    t, *q = map(int, input().split())
    if t == 1:
        tree.update_range(*q)
    else:
        print(tree.query(*q))
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

class SegTree:
    def __init__(self, n):
        cnt = n
        self.base = 1
        while n > 0:
            self.base <<= 1
            n >>= 1
        self.t = [[10 ** 9, 0] for i in range(self.base * 2)]
        for i in range(self.base, cnt + self.base):
            self.t[i][:] = (i - self.base, i - self.base)

        idx = self.base
        while idx > 0:
            for i in range(idx // 2, idx):
                self.t[i][0] = min(self.t[i * 2][0], self.t[i * 2 + 1][0])
                self.t[i][1] = max(self.t[i * 2][1], self.t[i * 2 + 1][1])
            idx >>= 1
        
    def swap(self, a, b):
        a += self.base; b += self.base
        self.t[a][:], self.t[b][:] = self.t[b][:], self.t[a][:]
        a >>= 1; b >>= 1

        while a > 0:
            self.t[a][0] = min(self.t[a * 2][0], self.t[a * 2 + 1][0])
            self.t[a][1] = max(self.t[a * 2][1], self.t[a * 2 + 1][1])

            if a != b:
                self.t[b][0] = min(self.t[b * 2][0], self.t[b * 2 + 1][0])
                self.t[b][1] = max(self.t[b * 2][1], self.t[b * 2 + 1][1])
            
            a >>= 1; b >>= 1

    def query(self, l, r):
        return self.__query(l, r, 0, self.base - 1, 1)
    
    def __query(self, l, r, s, e, idx):
        if r < s or e < l:
            return 10 ** 9, -1
        
        if l <= s and e <= r:
            return self.t[idx][0], self.t[idx][1]
        
        mid = (s + e) // 2
        lm, lM = self.__query(l, r, s, mid, idx * 2)
        rm, rM = self.__query(l, r, mid + 1, e, idx * 2 + 1)

        return min(lm, rm), max(lM, rM)

for _ in range(int(input())):
    n, k = map(int, input().split())
    tree = SegTree(n)
    for _ in range(k):
        q, a, b = map(int, input().split())
        if q == 0:
            tree.swap(a, b)
        else:
            m, M = tree.query(a, b)
            if (m, M) == (a, b):
                print('YES')
            else:
                print('NO')
import sys

input = sys.stdin.readline

class SegTree:
    def __init__(self, arr):
        n = len(arr)
        self.base = 1
        while n > 0:
            self.base <<= 1
            n >>= 1
        self.t = [[10 ** 2, -1] for _ in range(self.base * 2)]
        for i in range(len(arr)):
            self.update(i, arr[i])

    def update(self, idx, val):
        idx += self.base
        self.t[idx][0] = val
        self.t[idx][1] = idx - self.base
        idx >>= 1

        while idx > 0:
            if self.t[idx * 2][0] < self.t[idx * 2 + 1][0]:
                self.t[idx][0] = self.t[idx * 2][0]
                self.t[idx][1] = self.t[idx * 2][1]
            else:
                self.t[idx][0] = self.t[idx * 2 + 1][0]
                self.t[idx][1] = self.t[idx * 2 + 1][1]
            idx >>= 1

    def query(self, l, r):
        return self.__query(l, r, 0, self.base - 1, 1)

    def __query(self, l, r, s, e, idx):
        if r < s or e < l:
            return 10 ** 9, -1
        
        if l <= s and e <= r:
            return self.t[idx][0], self.t[idx][1]
        
        mid = (s + e) // 2
        l_val = self.__query(l, r, s, mid, idx * 2)
        r_val = self.__query(l, r, mid + 1, e, idx * 2 + 1)

        return min(l_val, r_val)
    
n = int(input())
sal = list(map(int, input().split()))
tree = SegTree(sal)
ans = 0
def query(l, r):
    global ans
    if l > r:
        return
    
    res = tree.query(l, r)
    ans = max(ans, (r - l + 1) * res[0])

    query(l, res[1] - 1)
    query(res[1] + 1, r)

query(0, n - 1)
print(ans)

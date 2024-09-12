import sys

input = sys.stdin.readline

class SegTree():
    def __init__(self, n, arr, default):
        size = 1
        while size < n:
            size <<= 1
        self.size = size << 1
        self.base = size
        self.default = default
        self.tree = [[-1, default] for _ in range(self.size)]
        for i in range(n):
            self.update(i, arr[i])

    def update(self, idx, val):
        idx += self.base
        self.tree[idx][:] = idx - self.base, val
        while idx > 1:
            idx >>= 1
            if self.tree[idx * 2][1] > self.tree[idx * 2 + 1][1]:
                self.tree[idx][:] = self.tree[idx * 2 + 1][:]
            else:
                self.tree[idx][:] = self.tree[idx * 2][:]
            
    def query(self, l, r):
        return self.__query_tb(0, self.base - 1, 1, l, r)
    
    def __query_tb(self, s, e, idx, l, r):
        if e < l or s > r:
            return -1, self.default
        if l <= s and e <= r:
            return self.tree[idx][0], self.tree[idx][1]
        mid = (s + e) // 2
        l_res = self.__query_tb(s, mid, idx * 2, l, r)
        r_res = self.__query_tb(mid + 1, e, idx * 2 + 1, l, r)
        if l_res[1] <= r_res[1]:
            return l_res
        else:
            return r_res


n = int(input())
arr = list(map(int, input().split()))

tree = SegTree(n, arr, 10 ** 10)

for _ in range(int(input())):
    x, i, j = map(int, input().split())
    if x == 1:
        tree.update(i - 1, j)
    else:
        print(tree.query(i - 1, j - 1)[0] + 1)
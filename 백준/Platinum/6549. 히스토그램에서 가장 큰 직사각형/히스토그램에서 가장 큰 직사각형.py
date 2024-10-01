import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

class SegTree:
    def __init__(self, arr):
        self.base = 1
        self.arr = arr + [10 ** 9 + 1]
        n = len(arr)
        while n > 0:
            self.base <<= 1
            n >>= 1
        self.t = [len(arr) for _ in range(self.base * 2)]

        for i in range(len(arr)):
            self.update(i, i)

    def update(self, idx, val):
        idx += self.base
        self.t[idx] = val
        idx >>= 1
        while idx > 0:
            if self.arr[self.t[idx * 2]] < self.arr[self.t[idx * 2 + 1]]:
                self.t[idx] = self.t[idx * 2]
            else:
                self.t[idx] = self.t[idx * 2 + 1]
            idx >>= 1
    
    def query(self, l, r):
        return self.__query(l, r, 0, self.base - 1, 1)

    def __query(self, l, r, s, e, idx):
        if r < s or e < l:
            return -1
        
        if l <= s and e <= r:
            return self.t[idx]

        mid = (s + e) // 2
        left = self.__query(l, r, s, mid, idx * 2)
        right = self.__query(l, r, mid + 1, e, idx * 2 + 1)
        
        if self.arr[left] > self.arr[right]:
            return right
        else:
            return left

def search(tree: SegTree, l, r):
    if l > r:
        return -1
    idx = tree.query(l, r)
    ans = tree.arr[idx] * (r - l + 1) if idx != -1 else 0
    l_val = search(tree, l, idx - 1)
    r_val = search(tree, idx + 1, r)
    return max(ans, l_val, r_val)

while True:
    n, *arr = map(int, input().split())
    if n == 0:
        break
    tree = SegTree(arr)
    print(search(tree, 0, n - 1))
class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.base = 1
        while n > 0:
            self.base <<= 1
            n >>= 1
        self.t = [0 for _ in range(self.base * 2)]
        for i in range(len(nums)):
            self.update(i, nums[i])

    def update(self, index: int, val: int) -> None:
        index += self.base
        diff = val - self.t[index]
        while index > 0:
            self.t[index] += diff
            index >>= 1
        
    def sumRange(self, left: int, right: int) -> int:
        return self.__sumRange(left, right, 0, self.base - 1, 1)

    def __sumRange(self, l, r, s, e, idx):
        if r < s or e < l:
            return 0
        
        if l <= s and e <= r:
            return self.t[idx]
        
        mid = (s + e) // 2
        l_val = self.__sumRange(l, r, s, mid, idx * 2)
        r_val = self.__sumRange(l, r, mid + 1, e, idx * 2 + 1)
        return l_val + r_val
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
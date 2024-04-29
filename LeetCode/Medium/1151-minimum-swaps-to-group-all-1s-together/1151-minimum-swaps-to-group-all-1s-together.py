import itertools

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        prefix_sum = [0] + list(itertools.accumulate(data))
        ones = data.count(1)
        min_diff = 999999
        st = 0
        for i in range(ones, len(data) + 1):
            if min_diff > ones - (prefix_sum[i] - prefix_sum[st]):
                min_diff = ones - (prefix_sum[i] - prefix_sum[st])
            st += 1
        return min_diff
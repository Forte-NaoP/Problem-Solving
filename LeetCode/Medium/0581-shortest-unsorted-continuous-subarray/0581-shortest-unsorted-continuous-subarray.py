class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort = sorted(nums)
        i, j = 0, len(nums) - 1
        
        while i < len(nums) and nums[i] == sort[i]:
            i += 1
        
        while j > 0 and nums[j] == sort[j]:
            j -= 1
        
        return max(j-i+1, 0)
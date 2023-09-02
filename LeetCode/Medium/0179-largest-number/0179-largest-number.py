class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        for i in range(len(nums)):
            nums[i] = (nums[i]*(10//len(nums[i]))+nums[i][:10%len(nums[i])], nums[i])
        nums.sort(reverse=True)
        answer = ''
        for num in nums:
            answer += num[1]
        
        return str(int(answer))

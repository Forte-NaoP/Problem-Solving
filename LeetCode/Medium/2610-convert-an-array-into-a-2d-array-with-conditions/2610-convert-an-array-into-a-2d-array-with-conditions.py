class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt_num = [0] * 201
        for num in nums:
            cnt_num[num] += 1
        
        max_group = max(cnt_num)
        ans = [[] for _ in range(max_group)]
        for i in range(1, 201):
            for j in range(cnt_num[i]):
                ans[j].append(i)
                
        return ans
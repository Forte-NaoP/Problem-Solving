class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i, k = 0, 0
        for group in groups:
            while i < len(nums):
                idx = i
                while idx < len(nums) and nums[idx] != group[0]:
                    idx += 1
                    
                if idx == len(nums) or idx + len(group) > len(nums):
                    return False
                
                found = True
                for j in range(len(group)):
                    if nums[idx+j] != group[j]:
                        found = False
                        i = idx + 1
                        break
                
                if not found:
                    continue
                
                i = idx + len(group)
                k += 1
                break
                
        
        if k == len(groups):
            return True
        else:
            return False

            
                
        
        
        
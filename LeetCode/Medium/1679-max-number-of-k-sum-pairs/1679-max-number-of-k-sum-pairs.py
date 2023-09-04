class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = dict()
        for num in nums:
            if count.get(num) is None:
                count[num] = 1
            else:
                count[num] += 1
        
        ans = 0
        for key in nums:
            pair = k - key
            if count.get(pair) is None:
                continue
            
            if pair == key:
                if count[key] >= 2:
                    count[key] -= 2
                    ans += 1
            else:
                if count[key] >= 1 and count[pair] >= 1:
                    count[key] -= 1
                    count[pair] -= 1
                    ans += 1
        return ans
        
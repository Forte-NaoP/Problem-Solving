class Solution:
    def minSwaps(self, s: str) -> int:
        one = s.count('1')
        zero = s.count('0')
        
        if not ((len(s) % 2 == 0 and one == zero) or (len(s) % 2 == 1 and abs(one - zero) == 1)):
            return -1
        
        zodd, zeven = 0, 0
        for i in range(len(s)):
            if s[i] == '0':
                if i % 2 == 0:
                    zeven += 1
                else:
                    zodd += 1

        odd, even = 0, 0
        for i in range(len(s)):
            if s[i] == '1':
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
        
        if len(s) % 2 == 0:
            return min(odd, even)
        else:
            if zodd == even:
                return even
            else:
                return odd
        
        
            
        
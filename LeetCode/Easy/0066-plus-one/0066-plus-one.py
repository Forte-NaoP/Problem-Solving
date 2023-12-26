class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = 0
        digits[0] += 1
        
        for i in range(len(digits)):
            s = digits[i] + carry
            carry = s // 10
            digits[i] = s % 10
        
        if carry != 0:
            digits.append(carry)
        
        digits.reverse()
        return digits
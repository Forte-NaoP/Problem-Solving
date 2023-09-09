class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        M = 0
        answer = 0
        for step, flip in enumerate(flips, start=1):
            M = max(M, flip)
            if M == step:
                answer += 1
        return answer
            
            
            
            
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        number = 1 << (len(flips)+1)
        refer = number
        answer = 0
        for step, flip in enumerate(flips):
            refer |= (1 << step)
            number |= (1 << (flip-1))
            if refer == number:
                answer += 1
        return answer
            
            
            
            
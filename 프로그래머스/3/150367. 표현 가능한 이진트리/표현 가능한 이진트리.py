def chk(num):
    if len(num) == 1 or '0' not in num or '1' not in num:
        return True
    
    mid = len(num) // 2
    if num[mid] == '0':
        return False
    
    return chk(num[:mid]) and chk(num[mid + 1:])
    
    

def extend(num):
    num_len = len(num)
    val = 1
    while num_len > val - 1:
        val *= 2
    
    num = '0' * (val - 1 - num_len) + num
    return num
    
def solution(numbers):
    answer = []
    bins = [2 ** i - 1 for i in range(51)]
    for num in numbers:
        num = bin(num)[2:]
        num_len = len(num)
        for bin_len in bins:
            if bin_len >= num_len:
                num = '0' * (bin_len - num_len) + num
                break
        
        answer.append(int(chk(num)))
        
    
    return answer
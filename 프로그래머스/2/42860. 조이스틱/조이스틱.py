def solution(name):
    length = len(name)
    diff = [min((ord(c) - ord('A')), (26 - (ord(c) - ord('A')))) for c in name]
    answer = sum(diff)
    
    move = length - 1
    for i in range(length):
        nxt = i + 1
        while nxt < length and diff[nxt] == 0:
            nxt += 1
        
        move = min((move, 2 * i + length - nxt, i + 2 * (length - nxt)))
    
    answer += move
    
    return answer
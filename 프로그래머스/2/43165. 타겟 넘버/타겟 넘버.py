def solution(numbers, target):
    answer = 0
    n = len(numbers)
    st = [(0, numbers[0]), (0, -numbers[0])]
    
    while st:
        idx, num = st.pop()
        idx += 1
        
        if idx < n:
            st.append((idx, num+numbers[idx]))
            st.append((idx, num-numbers[idx]))
        else:
            if num == target:
                answer += 1
        
    return answer
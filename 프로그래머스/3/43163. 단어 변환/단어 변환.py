from collections import deque

def solution(begin, target, words):
    
    word_dict = {}
    partial_dict = {}
    visit = set()
    
    word_len = len(words[0])
    words.append(begin)
    
    for word in words:
        part = [word[1:], word[:-1]]
        for i in range(1, word_len-1):
            part.append(word[0:i]+word[i+1:])
        
        for p in part:
            if word_dict.get(p) is None:
                word_dict[p] = [word]
            else:
                word_dict[p].append(word)
            
            if partial_dict.get(word) is None:
                partial_dict[word] = [p]
            else:
                partial_dict[word].append(p)
    
    q = deque([(begin, 0)])
    answer = 0
    
    while q:
        now, num = q.popleft()
        if now == target:
            answer = num
            break
            
        for part in partial_dict[now]:
            for nxt_word in word_dict[part]:
                if nxt_word not in visit:
                    q.append((nxt_word, num + 1))
                    visit.add(nxt_word)
        
    return answer
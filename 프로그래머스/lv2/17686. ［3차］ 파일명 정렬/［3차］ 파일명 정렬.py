def solution(files):
    answer = []
    digits = '0123456789'
    file_split = []
    for file in files:
        is_num = False
        num_i, num_j = 0, len(file)
        for idx, c in enumerate(file):
            if c in digits:
                if not is_num:
                    is_num = True
                    num_i = idx
            else:
                if is_num:
                    num_j = idx
                    break

        while num_j - num_i > 5:
            num_j -= 1
        
        file_split.append((file[:num_i].lower(), int(file[num_i:num_j]), file[:num_i], file[num_i:num_j], file[num_j:]))

    file_split.sort(key=lambda k: (k[0], k[1]))

    for hl, ni, h, n, t in file_split:
        answer.append(h+n+t)

    return answer
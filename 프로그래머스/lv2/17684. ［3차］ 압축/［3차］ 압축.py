def solution(msg):
    import string
    answer = []
    index_dict = dict()

    for idx, c in enumerate(string.ascii_uppercase, start=1):
        index_dict[c] = idx

    if len(msg) == 1:
        return [index_dict[msg]]

    idx += 1
    i, j = 0, 1

    while True:
        while j <= len(msg) and index_dict.get(msg[i:j]) is not None:
            j += 1

        answer.append(index_dict[msg[i:j-1]])
        index_dict[msg[i:j]] = idx
        idx += 1

        i = j-1
        j = i+1

        if j >= len(msg):
            break

    if i < len(msg):
        answer.append(index_dict[msg[i:]])

    return answer

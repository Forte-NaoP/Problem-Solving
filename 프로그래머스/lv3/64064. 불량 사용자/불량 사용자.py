def solution(user_id, banned_id):
    user_id = set(user_id)
    answer = set()

    def track(users, idx, banned):
        nonlocal answer

        if idx == len(banned_id):
            answer.add(''.join(sorted(banned)))
            return

        for user in users:
            if len(user) != len(banned_id[idx]):
                continue

            j = 0
            while j < len(user):
                if banned_id[idx][j] != '*' and user[j] != banned_id[idx][j]:
                    break
                j += 1

            if j == len(user):
                _users = users.copy()
                _users.remove(user)
                banned.append(user)
                track(_users, idx + 1, banned)
                banned.pop()


    track(user_id, 0, list())
    return len(answer)
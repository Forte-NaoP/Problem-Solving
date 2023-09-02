def solution(A, B):
    answer = 0
    B.sort()
    used = [i for i in range(len(B)+1)]

    def upper_bound(k):
        low, high = -1, len(B)
        while (low+1) < high:
            mid = (low + high) // 2

            if B[mid] <= k:
                low = mid
            else:
                high = mid
        return high

    for a in A:
        if (idx := upper_bound(a)) != len(B):
            while used[idx] != idx:
                idx = used[idx]
            if idx < len(B):
                answer += 1
                used[idx] = used[idx+1]
            else:
                used[idx] = len(B)
    return answer
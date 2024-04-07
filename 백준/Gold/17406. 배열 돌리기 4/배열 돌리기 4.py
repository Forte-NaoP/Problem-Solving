import sys
from itertools import permutations

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
_arr = [[0 for _ in range(m)] for _ in range(n)]
rotate_permute = [list(map(int, input().split())) for _ in range(k)]
rotate_permute = list(permutations(rotate_permute))

min_ans = 99999
for rotate_list in rotate_permute:
    for i in range(n):
        for j in range(m):
            _arr[i][j] = arr[i][j]
    
    for rotate in rotate_list:
        r, c, s = rotate
        r -= 1
        c -= 1

        for d in range(s, 0, -1):
            tmp_ne = _arr[r - d][c + d]
            for j in range(c + d, c - d, -1):
                _arr[r - d][j] = _arr[r - d][j - 1]

            tmp_se = _arr[r + d][c + d]
            for i in range(r + d, r - d + 1, -1):
                _arr[i][c + d] = _arr[i - 1][c + d]
            _arr[r - d + 1][c + d] = tmp_ne

            tmp_sw = _arr[r + d][c - d]
            for j in range(c - d, c + d - 1):
                _arr[r + d][j] = _arr[r + d][j + 1]
            _arr[r + d][c + d - 1] = tmp_se

            for i in range(r - d, r + d - 1):
                _arr[i][c - d] = _arr[i + 1][c - d]
            _arr[r + d - 1][c - d] = tmp_sw


    min_arr = 99999
    for i in range(n):
        min_arr = min(min_arr, sum(_arr[i]))
    
    min_ans = min(min_ans, min_arr)

print(min_ans)
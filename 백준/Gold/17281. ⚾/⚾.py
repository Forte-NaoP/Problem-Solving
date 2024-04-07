import sys
from itertools import permutations

n = int(input())
inning_result = [list(map(int, input().split())) for _ in range(n)]

entry_list = list(map(list, permutations([1, 2, 3, 4, 5, 6, 7, 8])))

score = -1
for entry in entry_list:
    entry.insert(3, 0)
    entry_idx = 0
    inning = 0
    entry_score = 0
    while inning < n: 
        out = 0
        b1 = b2 = b3 = 0
        while out < 3:
            hit_kind = inning_result[inning][entry[entry_idx]]
            if hit_kind == 0:
                out += 1
            else:
                if hit_kind == 1:
                    entry_score += b3
                    b1, b2, b3 = 1, b1, b2
                elif hit_kind == 2:
                    entry_score += b3 + b2
                    b1, b2, b3 = 0, 1, b1
                elif hit_kind == 3:
                    entry_score += b3 + b2 + b1
                    b1, b2, b3 = 0, 0, 1
                else:
                    entry_score += b3 + b2 + b1 + 1
                    b1, b2, b3 = 0, 0, 0
            entry_idx = (entry_idx + 1) % 9
        inning += 1
    score = max(score, entry_score)

print(score)
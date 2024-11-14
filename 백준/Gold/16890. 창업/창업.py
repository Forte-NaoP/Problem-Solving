import sys
from collections import deque

input = lambda : sys.stdin.readline().strip()

koo = sorted(input())
cube = sorted(input(), reverse=True)

title_len = len(koo)
title = ['?' for _ in range(title_len)]

koo = deque(koo[:title_len - title_len // 2])
cube = deque(cube[:title_len // 2])

s_idx, e_idx = 0, title_len - 1
man = [koo, cube]
turn = 0

for _ in range(title_len):
    if koo and cube and koo[0] >= cube[0]:
        title[e_idx] = man[turn].pop()
        e_idx -= 1
    else:
        title[s_idx] = man[turn].popleft()
        s_idx += 1
    turn ^= 1

print(''.join(title))


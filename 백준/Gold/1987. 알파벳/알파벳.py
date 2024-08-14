import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline
r, c = map(int, input().split())
row, col = range(r), range(c)
board = [list(input().strip()) for _ in row]

diff = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs():
    v = 1 << (ord(board[0][0]) - 65)
    q = set([(0, 0, v)])
    ans = v.bit_count()
    while q:
        x, y, v = q.pop()
        ans = max(ans, v.bit_count())
        for dx, dy in diff:
            nx, ny = x + dx, y + dy
            if nx not in row or ny not in col:
                continue
            if v & (1 << (ord(board[nx][ny]) - 65)):
                continue
            q.add((nx, ny, v | (1 << (ord(board[nx][ny]) - 65))))

    return ans

print(bfs())

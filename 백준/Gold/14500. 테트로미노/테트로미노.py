import sys
input = sys.stdin.readline

tetros = [
    [(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1)], [(0, 0), (0, 1), (0, 2), (1, 0)], [(0, 0), (0, 1), (1, 1), (2, 1)], [(0, 0), (1, 0), (1, -1), (1, -2)],
    [(0, 0), (1, 0), (2, 0), (2, -1)], [(0, 0), (1, 0), (1, 1), (1, 2)], [(0, 0), (0, 1), (1, 0), (2, 0)], [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 1)], [(0, 0), (0, 1), (1, 0), (1, -1)],
    [(0, 0), (1, 0), (1, -1), (2, -1)], [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 1)], [(0, 0), (1, 0), (2, 0), (1, -1)], [(0, 0), (1, 0), (1, -1), (1, 1)], [(0, 0), (1, 0), (2, 0), (1, 1)],
]
n, m = map(int, input().split())
row, col = range(n), range(m)
paper = [list(map(int, input().split())) for _ in row]

def calc(x, y, tetro):
    score = 0
    for dx, dy in tetro:
        nx, ny = x + dx, y + dy
        if nx not in row or ny not in col:
            return 0
        score += paper[nx][ny]
    return score

score = 0
for i in row:
    for j in col:
        for tetro in tetros:
            score = max(score, calc(i, j, tetro))

print(score)

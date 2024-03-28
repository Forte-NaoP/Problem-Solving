import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
tile = [list(map(int, input().split())) for _ in range(n)]
cmd = list(map(int, input().split()))
mv = [(0, 1), (0, -1), (-1, 0), (1, 0)]

dice = [[0 for _ in range(4)] for _ in range(4)]

def roll(d):
    global x, y, n, m

    if not ((0 <= x + mv[d][0] < n) and (0 <= y + mv[d][1] < m)):
        return False
    
    x += mv[d][0]
    y += mv[d][1]

    if d == 0:
        t = dice[1][3]
        for i in range(3, 0, -1):
            dice[1][i] = dice[1][i - 1]
        dice[1][0] = t
        dice[3][1] = dice[1][3]
    elif d == 1:
        t = dice[1][0]
        for i in range(3):
            dice[1][i] = dice[1][i + 1]
        dice[1][3] = t
        dice[3][1] = dice[1][3]
    elif d == 2:
        t = dice[0][1]
        for i in range(3):
            dice[i][1] = dice[i + 1][1]
        dice[3][1] = t
        dice[1][3] = dice[3][1]
    else:
        t = dice[3][1]
        for i in range(3, 0, -1):
            dice[i][1] = dice[i - 1][1]
        dice[0][1] = t
        dice[1][3] = dice[3][1]
    
    if tile[x][y] == 0:
        tile[x][y] = dice[3][1]
    else:
        dice[3][1] = dice[1][3] = tile[x][y]
        tile[x][y] = 0
    
    return True

for c in cmd:
    if roll(c - 1):
        print(dice[1][1])
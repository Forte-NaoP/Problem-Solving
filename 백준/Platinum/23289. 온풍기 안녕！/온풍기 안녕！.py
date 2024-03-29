import sys
from collections import deque

input = sys.stdin.readline

row_num, col_num, k = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(row_num)]
heater = [[], [], [], []]
heater_map = [[0 for _ in range(col_num)] for _ in range(row_num)]
heat_tmp = [[0 for _ in range(col_num)] for _ in range(row_num)]
wall = [[0 for _ in range(col_num)] for _ in range(row_num)]
temp = [[0 for _ in range(col_num)] for _ in range(row_num)]
chk = []

RIGHT, LEFT, UP, DOWN = 1, 2, 4, 8

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(row_num):
    for j in range(col_num):
        if room[i][j] > 0:
            if room[i][j] < 5:
                heater[room[i][j] - 1].append((i, j))
            else:
                chk.append((i, j))

w = int(input())
for _ in range(w):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    if t == 0:
        wall[x][y] |= UP
        wall[x - 1][y] |= DOWN
    else:
        wall[x][y] |= RIGHT
        wall[x][y + 1] |= LEFT

row = range(row_num)
col = range(col_num)

q = deque()
for d, h in enumerate(heater):
    DIRECTION = (1 << d)
    for x, y in h:
        if wall[x][y] & DIRECTION:
            continue
        q.append((x + dx[d], y + dy[d], 5))
        while q:
            cx, cy, nt = q.popleft()
            heat_tmp[cx][cy] = nt
            if nt == 1:
                continue
            ncx, ncy = cx + dx[d], cy + dy[d]
            if d < 2: # 횡방향
                if ncy not in col:
                    continue
                if not (wall[cx][cy] & DIRECTION):
                    q.append((ncx, ncy, nt - 1))
                if ncx - 1 in row and not (wall[cx][cy] & UP) and not (wall[ncx - 1][cy] & DIRECTION):
                    q.append((ncx - 1, ncy, nt - 1))
                if ncx + 1 in row and not (wall[cx][cy] & DOWN) and not (wall[ncx + 1][cy] & DIRECTION):
                    q.append((ncx + 1, ncy, nt - 1))
            else: # 종방향
                if ncx not in row:
                    continue
                if not (wall[cx][cy] & DIRECTION):
                    q.append((ncx, ncy, nt - 1))
                if ncy - 1 in col and not (wall[cx][cy] & LEFT) and not (wall[cx][ncy - 1] & DIRECTION):
                    q.append((ncx, ncy - 1, nt - 1))
                if ncy + 1 in col and not (wall[cx][cy] & RIGHT) and not (wall[cx][ncy + 1] & DIRECTION):
                    q.append((ncx, ncy + 1, nt - 1))
        for x in row:
            for y in col:
                heater_map[x][y] += heat_tmp[x][y]
                heat_tmp[x][y] = 0

def blow():
    for x in row:
        for y in col:
            temp[x][y] += heater_map[x][y]

def adjust():
    for x in row:
        for y in col:
            for i in range(4):
                if wall[x][y] & (1 << i):
                    continue
                nx, ny = x + dx[i], y + dy[i]
                if nx in row and ny in col and temp[x][y] > temp[nx][ny]:
                    heat_tmp[nx][ny] += (temp[x][y] - temp[nx][ny]) // 4
                    heat_tmp[x][y] -= (temp[x][y] - temp[nx][ny]) // 4

    for x in row:
        for y in col:
            temp[x][y] += heat_tmp[x][y]
            heat_tmp[x][y] = 0

def cool():
    for i in row:
        temp[i][0] = max(0, temp[i][0] - 1)
        temp[i][-1] = max(0, temp[i][-1] - 1)
    
    for j in range(1, col_num - 1):
        temp[0][j] = max(0, temp[0][j] - 1)
        temp[-1][j] = max(0, temp[-1][j] - 1)

def check():
    for x, y in chk:
        if temp[x][y] < k:
            return False
    return True

chocolate = 0
while not check() and chocolate <= 100:
    blow()
    adjust()
    cool()
    chocolate += 1

print(chocolate)
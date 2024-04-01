import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
room_tmp = [[0 for _ in range(c)] for _ in range(r)]

row = range(r)
col = range(c)

hx, lx= -1, -1

for i in range(r):
    if room[i][0] == -1:
        hx, hy = i, 0
        lx, ly = i + 1, 0
        break

def diffuse():
    for i in row:
        for j in col:
            if room[i][j] > 0:
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if (nx in row) and (ny in col) and room[nx][ny] != -1:
                        room_tmp[nx][ny] += room[i][j] // 5
                        room_tmp[i][j] -= room[i][j] // 5

    for i in row:
        for j in col:
            room[i][j] += room_tmp[i][j]
            room_tmp[i][j] = 0

def clean():
    global r, c, hx, lx

    for i in range(hx, 0, -1):
        room[i][0] = room[i - 1][0]
    for j in range(1, c):
        room[0][j - 1] = room[0][j]
    for i in range(hx):
        room[i][-1] = room[i + 1][-1]
    for j in range(c - 1, 0, -1):
        room[hx][j] = room[hx][j - 1]
    room[hx][1] = 0
    room[hx][0] = -1

    for i in range(lx + 1, r - 1):
        room[i][0] = room[i + 1][0]
    for j in range(c - 1):
        room[-1][j] = room[-1][j + 1]
    for i in range(r - 1, lx, -1):
        room[i][-1] = room[i - 1][-1]
    for j in range(c - 1, 0, -1):
        room[lx][j] = room[lx][j - 1]
    room[lx][1] = 0
    room[lx][0] = -1

for _ in range(t):
    diffuse()
    clean()

dust = 0
for i in row:
    for j in col:
        dust += room[i][j]
print(dust + 2)

import sys
from collections import deque

INF = 1e9
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, remain = map(int, input().split())
row = col = range(n)
sea = [list(map(int, input().split())) for _ in row]
look = [-1] + list(map(lambda x: int(x) - 1, input().split()))

shark = {}
for i in row:
    for j in col:
        if sea[i][j] != 0:
            shark[sea[i][j]] = [i, j, look[sea[i][j]]]

pshark = [[]]
smell_chk = set()
smell_volatile = deque()
smell = [[[0, 0] for _ in col] for _ in row]

for _ in range(m):
    pshark.append([])
    for _ in range(4):
        pshark[-1].append(list(map(lambda x: int(x) - 1, input().split())))


def find_nxt(idx, empty):
    x, y, d = shark[idx]

    for pd in pshark[idx][d]:
        nx, ny = x + dx[pd], y + dy[pd]
        if nx not in row or ny not in col:
            continue
        if empty:
            if smell[nx][ny][1] == 0:
                return True, nx, ny, pd
        else:
            if smell[nx][ny][0] == idx:
                return True, nx, ny, pd
    return False, -1, -1, -1

def move(idx):
    x, y, d = shark[idx]
    
    can_move, nx, ny, nd = find_nxt(idx, True)
    if not can_move:
        can_move, nx, ny, nd = find_nxt(idx, False)

    shark[idx][0] = nx
    shark[idx][1] = ny
    shark[idx][2] = nd
    sea[x][y] = 0

total = m
banned = [False for _ in range(m + 1)]
def ban():
    global total
    for k in shark.keys():
        if banned[k]:
            continue
        x, y, d = shark[k]
        if sea[x][y] == 0:
            sea[x][y] = k
        elif sea[x][y] < k:
            banned[k] = True
            total -= 1
        else:
            banned[sea[x][y]] = True
            total -= 1
            sea[x][y] = k

def mark():
    global remain

    for (sx, sy) in smell_chk:
        smell[sx][sy][1] -= 1
        if smell[sx][sy][1] == 0:
            smell[sx][sy][0] = 0
            smell[sx][sy][1] = 0
            smell_volatile.append((sx, sy))

    while smell_volatile:
        smell_chk.remove(smell_volatile.pop())

    for k in shark.keys():
        if banned[k]:
            continue
        x, y, _ = shark[k]
        smell[x][y][0] = k
        smell[x][y][1] = remain
        smell_chk.add((x, y))

sec = 0
mark()
while sec < 1001 and total > 1:
    for k in shark.keys():
        if banned[k]:
            continue
        move(k)
    ban()
    mark()
    sec += 1

if sec == 1001:
    sec = -1
print(sec)
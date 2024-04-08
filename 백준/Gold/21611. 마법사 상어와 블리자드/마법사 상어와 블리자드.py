import sys
from collections import deque, defaultdict

n, m = map(int, input().split())
cx = cy = n // 2
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

row = col = range(n)

grid = [list(map(int, input().split())) for _ in range(n)]
test = [[0 for _ in range(n)] for _ in range(n)]
grid_num = []
max_num = n ** 2

def make_num(n):
    cnt = n ** 2 - 1    
    x, y = 0, 0
    xh, yh, xl, yl = n, n, 0, -1

    x, y = 0, 0
    while cnt > 0:
        while y < yh:
            grid_num.append((cnt, x, y))
            cnt -= 1
            y += 1

        x, y = x + 1, y - 1
        while x < xh:
            grid_num.append((cnt, x, y))
            cnt -= 1
            x += 1

        x, y = x - 1, y - 1
        while y > yl:
            grid_num.append((cnt, x, y))
            cnt -= 1
            y -= 1

        x, y = x - 1, y + 1
        while x > xl + 1:
            grid_num.append((cnt, x, y))
            cnt -= 1
            x -= 1
        xh, yh, xl, yl = xh - 1, yh - 1, xl + 1, yl + 1

    grid_num.sort()

make_num(n)

for cnt, x, y in grid_num:
    test[x][y] = cnt

def blizzard(d, s):
    global cx, cy
    x, y = cx + dx[d], cy + dy[d]
    for _ in range(s):
        if x not in row or y not in col:
            break
        grid[x][y] = 0
        x += dx[d]
        y += dy[d]

score = 0
def boom():
    global score, max_num
    streak, streak_num = 0, 0
    result = False
    for cnt, x, y in grid_num:
        if grid[x][y] != 0:
            if streak_num == grid[x][y]:
                streak += 1
            else:
                if streak >= 4:
                    result = True
                    score += streak * streak_num
                    idx = cnt - 1
                    while streak > 0:
                        _, _x, _y = grid_num[idx]
                        if grid[_x][_y] == streak_num:
                            grid[_x][_y] = 0
                            streak -= 1
                        idx -= 1
                streak = 1
                streak_num = grid[x][y]
    
    if streak >= 4:
        result = True
        score += streak * streak_num
        idx = len(grid_num) - 1
        while streak > 0:
            _, _x, _y = grid_num[idx]
            if grid[_x][_y] != 0:
                grid[_x][_y] = 0
                streak -= 1
            idx -= 1

    return result

g = deque()

def group():
    streak, streak_num = 0, 0
    for _, x, y in grid_num:
        if grid[x][y] != 0:
            if streak_num == grid[x][y]:
                streak += 1
            else:
                if streak_num != 0:
                    g.append((streak, streak_num))
                streak = 1
                streak_num = grid[x][y]
    if streak_num != 0:
        g.append((streak, streak_num))


def printarr(arr):
    for a in arr:
        print(a)
    print()

for _ in range(m):
    d, s = map(int, input().split())

    blizzard(d - 1, s)

    while boom():
        pass

    group()

    for i in range(1, len(grid_num), 2):
        if g:
            a, b = g.popleft()
            grid[grid_num[i][1]][grid_num[i][2]] = a
            grid[grid_num[i + 1][1]][grid_num[i + 1][2]] = b
        else:
            grid[grid_num[i][1]][grid_num[i][2]] = 0
            grid[grid_num[i + 1][1]][grid_num[i + 1][2]] = 0
    g.clear()

print(score)

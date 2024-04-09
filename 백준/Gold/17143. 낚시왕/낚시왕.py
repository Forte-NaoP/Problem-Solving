import sys
from collections import deque, defaultdict

r, c, m = map(int, input().split())
row, col = range(r), range(c)
row_num = [i for i in row] + [i for i in range(r - 2, 0, -1)]
col_num = [i for i in col] + [i for i in range(c - 2, 0, -1)]
diff = [(-1, 0), (1, 0), (0, 1), (0, -1)]
grid = [[0 for _ in col] for _ in row]
king = -1
shark = {}

for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    grid[x - 1][y - 1] = z
    shark[z] = [x - 1, y - 1, diff[d - 1][0] * s, diff[d - 1][1] * s, z]

def init():
    for i in row:
        for j in col:
            grid[i][j] = 0

catch = 0
while king < c:
    king += 1
    if king == c:
        break

    for i in row:
        if grid[i][king] != 0:
            catch += grid[i][king]
            shark[grid[i][king]][4] = -1
            grid[i][king] = 0
            break

    for k in shark.keys():
        if shark[k][4] == -1:
            continue

        x, y, dx, dy, z = shark[k]
        
        nx = row_num[(x + dx) % (2 * (r - 1))]
        ny = col_num[(y + dy) % (2 * (c - 1))]

        if (x + dx) % (2 * (r - 1)) >= r:
            dx = -dx
        if (y + dy) % (2 * (c - 1)) >= c:
            dy = -dy

        shark[k][0] = nx 
        shark[k][1] = ny 
        shark[k][2] = dx
        shark[k][3] = dy

    init()
    for k in shark.keys():
        if shark[k][4] == -1:
            continue
        x, y, = shark[k][0], shark[k][1]
        if grid[x][y] == 0:
            grid[x][y] = shark[k][4]
        elif grid[x][y] > shark[k][4]:
            shark[k][4] = -1
        else:
            shark[grid[x][y]][4] = -1
            grid[x][y] = shark[k][4]

print(catch)
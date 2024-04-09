import sys
from collections import deque, defaultdict

n, m = map(int, input().split())
row = col = range(n)
game = [list(map(lambda x: int(x) if int(x) != 0 else 9, input().split())) for _ in row]
game = [game, [[0 for _ in col] for _ in row]]
diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visit = [[0 for _ in col] for _ in row]
group = [[[] for _ in col] for _ in row]
gidx = 0

def rotate():
    global gidx, n
    gidx ^= 1
    for i in row:
        for j in col:
            game[gidx][n - j - 1][i] = game[gidx ^ 1][i][j]

def fall_down():
    global gidx, n

    for j in col:
        bottom = n - 1
        i = n - 1
        while bottom >= 0:
            while bottom >= 0 and game[gidx][bottom][j] != 0:
                bottom -= 1
            if bottom == - 1:
                break
            
            if bottom <= i:
                i = bottom - 1

            while i >= 0 and game[gidx][i][j] == 0:
                i -= 1
            if i == -1:
                break

            if game[gidx][i][j] == -1:
                bottom = i - 1
                continue
            game[gidx][bottom][j] = game[gidx][i][j]
            game[gidx][i][j] = 0
            bottom -= 1
            i -= 1

q = deque()
bfs_num = 1
def bfs(x, y, c, i):
    global gidx
    
    rb, nb = 0, 1
    group[x][y].clear()

    q.append((x, y))
    visit[x][y] = i
    group[x][y].append((x, y))
    
    while q:
        cx, cy = q.popleft()
        
        for dx, dy in diff:
            nx, ny = cx + dx, cy + dy
            if (nx not in row) or (ny not in col) or (visit[nx][ny] == i):
                continue
            if (game[gidx][nx][ny] != c and game[gidx][nx][ny] != 9):
                continue
            q.append((nx, ny))
            visit[nx][ny] = i
            group[x][y].append((nx, ny))
            if game[gidx][nx][ny] == c:
                nb += 1
            else:
                rb += 1
                
    for bx, by in group[x][y]:
        if game[gidx][bx][by] == 9:
            visit[bx][by] = 0
    
    if nb > 0 and nb + rb > 1:
        return (True, ((nb + rb), rb, x, y))
    else:
        return (False, (None, None, None, None))

score = 0
while True:
    res = (-1, -1, -1, -1)
    for i in row:
        for j in col:
            if visit[i][j] != 0 and visit[i][j] == bfs_num:
                continue
            if game[gidx][i][j] == 0 or game[gidx][i][j] == -1 or game[gidx][i][j] == 9:
                continue

            r, bfs_res = bfs(i, j, game[gidx][i][j], bfs_num)
            if r:
                res = max(res, bfs_res)

    if res[0] == -1:
        break
    tb, rb, x, y = res
    score += tb ** 2
    for bx, by in group[x][y]:
        game[gidx][bx][by] = 0
    
    fall_down()
    rotate()
    fall_down()

    bfs_num += 1

print(score)

import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

direct = [(-1, 0), (0, -1), (0, 1), (1, 0)]

graph = defaultdict(lambda : [(-1, -1)] * 4)
visit = defaultdict(lambda : False)
red, blue, hole = (), (), ()

for i in range(1, n - 1):
    for j in range(1, m - 1):
        if board[i][j] == '#':
            continue
        if board[i][j] == 'R':
            red = (i, j)
        elif board[i][j] == 'B':
            blue = (i, j)
        elif board[i][j] == 'O':
            hole = (i, j)
        else:
            pass

        for d, (dx, dy) in enumerate(direct):
            nx, ny = i, j
            is_hole = False
            while board[nx + dx][ny + dy] != '#':
                nx += dx
                ny += dy
                if board[nx][ny] == 'O':
                    hole = (nx, ny)
                    is_hole = True
                    break
            if (nx != i) or (ny != j):
                if is_hole:
                    graph[(i, j)][d] = hole
                else:
                    graph[(i, j)][d] = (nx, ny)
            else:
                graph[(i, j)][d] = (i, j)

q = deque()
q.append((*red, *blue, 0))
visit[(*red, *blue)] = True
ans = 11
while q:
    rx, ry, bx, by, cnt = q.popleft()
    if cnt > 10 :
        break
    for d, (dx, dy) in enumerate(direct):
        nrx, nry = graph[(rx, ry)][d]
        nbx, nby = graph[(bx, by)][d]
        if visit[(nrx, nry, nbx, nby)] or hole == (nbx, nby):
            continue
        if nrx == nbx and nry == nby:
            if abs(rx - nrx) + abs(ry - nry) > abs(bx - nbx) + abs(by - nby):                
                nrx -= dx
                nry -= dy
            else:
                nbx -= dx
                nby -= dy
            q.append((nrx, nry, nbx, nby, cnt + 1))
            visit[(nrx, nry, nbx, nby)] = True
        else:
            if hole == (nrx, nry):
                ans = min(ans, cnt + 1)
                continue
            q.append((nrx, nry, nbx, nby, cnt + 1))
            visit[(nrx, nry, nbx, nby)] = True

if ans > 10:
    print(-1)
else:
    print(ans)
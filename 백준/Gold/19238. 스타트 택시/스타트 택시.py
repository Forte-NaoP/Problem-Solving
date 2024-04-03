import sys
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop

INF = 1e9
diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n, m, fuel = map(int, input().split())
wall = [list(map(lambda x: False if x == '0' else True, input().split())) for _ in range(n)]
wait = [[set() for _ in range(n)] for _ in range(n)]
visit = [[False for _ in range(n)] for _ in range(n)]
tx, ty = map(lambda x: int(x) - 1, input().split())

row = col = range(n)

guest = defaultdict(list)
dst = [(tx, ty)]
for i in range(1, m + 1):
    sx, sy, dx, dy = map(lambda x: int(x) - 1, input().split())
    wait[sx][sy].add(i)
    wait[dx][dy].add(-i)
    dst.append((dx, dy))

dist = defaultdict(list)
q = deque()

def bfs(idx):
    global n
    for i in range(n):
        for j in range(n):
            visit[i][j] = False

    x, y = dst[idx]
    q.append((x, y, 0))
    visit[x][y] = True

    while q:
        cx, cy, d = q.popleft()
        for who in wait[cx][cy]:
            if who < 0:
                continue
            if who == idx:
                guest[(cx, cy)] = [x, y, d]
            else:
                hpush(dist[(x, y)], (d, cx, cy, who))
        
        for dx, dy in diff:
            nx, ny = cx + dx, cy + dy
            if nx in row and ny in col and not visit[nx][ny] and not wall[nx][ny]:
                q.append((nx, ny, d + 1))
                visit[nx][ny] = True
    
for idx in range(len(dst)):
    bfs(idx)
    
carried = set()
while dist[(tx, ty)] and len(carried) < m:

    d, nx, ny, idx = hpop(dist[(tx, ty)])
    while idx in carried and dist[(tx, ty)]:
        d, nx, ny, idx = hpop(dist[(tx, ty)])

    if d > fuel:
        break
    fuel -= d

    if not guest[(nx, ny)]:
        break

    dx, dy, cost = guest[(nx, ny)]
    if cost > fuel:
        break

    fuel += cost

    tx, ty = dx, dy
    carried.add(idx)

if len(carried) != m:
    fuel = -1
print(fuel)

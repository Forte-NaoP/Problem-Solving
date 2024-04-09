import sys
from collections import deque, defaultdict

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
row = col = range(n)
grid = [[[] for _ in col] for _ in row]
queue = deque()
chk = set()

for _ in range(m):
    r, c, mass, s, d = map(int, input().split())
    queue.append((r - 1, c - 1, mass, s, d))

def move():
    global n

    chk.clear()
    while queue:
        x, y, m, s, d = queue.popleft()
        x, y = (x + dx[d] * s) % n, (y + dy[d] * s) % n
        grid[x][y].append((x, y, m, s, d))
        chk.add((x, y))

    for x, y in chk:
        if len(grid[x][y]) == 1:
            queue.append(*grid[x][y])
            grid[x][y].clear()
        else:
            tm, ts, te, to = 0, 0, 0, 0
            for _, _, m, s, d in grid[x][y]:
                tm += m
                ts += s
                if d % 2 == 0:
                    te += 1
                else:
                    to += 1
            tm //= 5
            if tm != 0:
                ts //= (te + to)
                odd = 1
                if te == 0 or to == 0:
                    odd = 0
                for i in range(0, 8, 2):
                    queue.append((x, y, tm, ts, i + odd))                 
            grid[x][y].clear()

for _ in range(k):
    move()

tm = 0
while queue:
    _, _, mass, _, _ = queue.popleft()
    tm += mass

print(tm)

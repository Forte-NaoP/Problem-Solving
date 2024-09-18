import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
row = range(r)
col = range(c)
lake = [list(input().strip()) for _ in row]
diff = [(0, -1), (1, 0), (0, 1), (-1, 0)]
g_idx = 1
group = [[-1 for _ in col] for _ in row]
chk = [[False for _ in col] for _ in row]
parent = dict()

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    
    parent[x] = y
    return True

melt = [[], []]
m_idx = 0
q = deque()
def bfs(x, y, idx):
    q.append((x, y))
    group[x][y] = idx
    if idx not in parent:
        parent[idx] = idx

    while q:
        x, y = q.popleft()

        for dx, dy in diff:
            nx, ny = x + dx, y + dy
            if nx not in row or ny not in col:
                continue
            if group[nx][ny] == idx:
                continue
            group[nx][ny] = idx
            if lake[nx][ny] == '.':
                q.append((nx, ny))
            else:
                melt[m_idx].append((idx, nx, ny))
                chk[nx][ny] = True

def meltdown():
    global m_idx
    while melt[m_idx]:
        idx, x, y = melt[m_idx].pop()
        group[x][y] = idx
        for dx, dy in diff:
            nx, ny = x + dx, y + dy
            if nx not in row or ny not in col:
                continue
            if group[nx][ny] == idx:
                continue
            if group[nx][ny] != -1:
                union(idx, group[nx][ny])
            elif not chk[nx][ny]:
                # group[nx][ny] = idx
                melt[m_idx ^ 1].append((idx, nx, ny))
                chk[nx][ny] = True
    m_idx ^= 1
    
x1, y1, x2, y2 = -1, -1, -1, -1
for i in row:
    for j in col:
        if lake[i][j] == 'L':
            if x1 == -1:
                x1, y1 = i, j
            else:
                x2, y2 = i, j
            lake[i][j] = '.'
        if lake[i][j] == '.' and group[i][j] == -1:
            bfs(i, j, g_idx)
            g_idx += 1

days = 0
while find(group[x1][y1]) != find(group[x2][y2]):
    meltdown()
    days += 1

print(days)
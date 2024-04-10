import sys
from collections import deque

n, lb, ub = map(int, input().split())
p_range = range(lb, ub + 1)
row = col = range(n)
diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]

world = [list(map(int, input().split())) for _ in row]
visit = [[-1 for _ in col] for _ in row]

q = deque()
group_queue = deque()

def bfs(x, y, bfs_id):
    visit[x][y] = bfs_id
    q.append((x, y))
    union = 0
    popular = 0

    while q:
        cx, cy = q.popleft()
        union += 1
        popular += world[cx][cy]
        group_queue.append((cx, cy))

        for dx, dy in diff:
            nx, ny = cx + dx, cy + dy
            if nx not in row or ny not in col:
                continue
            if abs(world[cx][cy] - world[nx][ny]) not in p_range:
                continue
            if visit[nx][ny] == bfs_id:
                continue
            visit[nx][ny] = bfs_id
            q.append((nx, ny))

    popular //= union
    while group_queue:
        x, y = group_queue.popleft()
        world[x][y] = popular
    if union > 1:
        return True
    else:
        return False

def printarr(arr):
    for a in arr:
        print(a)
    print()

day = 0

while True:
    moved = False
    for i in row:
        for j in col:
            if visit[i][j] == day:
                continue
            moved |= bfs(i, j, day)
    if not moved:
        break
    day += 1 

print(day)
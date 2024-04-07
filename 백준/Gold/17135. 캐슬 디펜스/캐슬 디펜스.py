import sys
from collections import deque
from copy import deepcopy

n, m, d = map(int, input().split())
visit = [[0 for _ in range(m)] for _ in range(n)]
diff = [(0, -1), (1, 0), (0, 1)]

init_field = deque()
total, eliminate = 0, 0
for _ in range(n):
    row = list(map(int, input().split()))
    total += row.count(1)
    init_field.appendleft(row)

q = deque()
bfs_cnt = 0
def bfs(start, n, field: deque):
    global m, d, bfs_cnt
    bfs_cnt += 1
    q.clear()
    q.append((0, start, 1))
    visit[0][start] = bfs_cnt
    while q:
        x, y, r = q.popleft()
        if field[x][y] == 1:
            return (x, y)
        if r == d:
            continue
        for dx, dy in diff:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n) and (0 <= ny < m) and visit[nx][ny] != bfs_cnt:
                q.append((nx, ny, r + 1))
                visit[nx][ny] = bfs_cnt
    return (-1, -1)

dead = []
def defence(place: list, field: deque):
    global total, eliminate, n
    c_total = total
    c_eliminate = 0

    left_line = n
    while c_total > 0 and left_line > 0:
        for p in place:
            x, y = bfs(p, left_line, field)
            if x != -1:
                dead.append((x, y))
        
        while dead:
            x, y = dead.pop()
            if field[x][y] == 1:
                field[x][y] = 0
                c_eliminate += 1
                c_total -= 1
        
        c_total -= field[0].count(1)
        field.popleft()
        left_line -= 1

    eliminate = max(eliminate, c_eliminate)


def search(place: list, last = -1):
    global m
    if len(place) == 3:
        field = deepcopy(init_field)
        defence(place, field)
        return
    
    place_copy = deepcopy(place)
    for i in range(last + 1, m):
        place_copy.append(i)
        search(place_copy, i)
        place_copy.pop()

search([])
print(eliminate)
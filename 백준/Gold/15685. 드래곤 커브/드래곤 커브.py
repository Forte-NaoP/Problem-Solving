import sys
from collections import deque

def evolve(curve: deque):
    px, py = curve[0]

    child = list(map(lambda p : [p[1] - py + px, -p[0] + px + py], curve))
    
    for i in range(1, len(child)):
        curve.appendleft(child[i])

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
grid = [[0 for _ in range(101)] for _ in range(101)]

n = int(input())

for i in range(n):
    y, x, d, g = map(int, input().split())
    curve = deque()
    curve.appendleft([x, y])
    curve.appendleft([x + dx[d], y + dy[d]])
    for _ in range(g):
        evolve(curve)
    for px, py in curve:
        grid[px][py] = True

ans = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i + 1][j] and grid[i][j + 1] and grid[i + 1][j + 1]:
            ans += 1

print(ans)
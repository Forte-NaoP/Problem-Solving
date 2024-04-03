import sys
from collections import deque

INF = 1e9
diff = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

n, m, k = map(int, input().split())
row = col = range(n)
food = [list(map(int, input().split())) for _ in row]
land = [[5 for _ in col] for _ in row]
tree = [[deque() for _ in col] for _ in row]
total = m

for _ in range(m):
    x, y, age = map(int, input().split())
    x -= 1
    y -= 1
    tree[x][y].append(age)

def spring_summer():
    global n, total
    for i in row:
        for j in col:
            k = 0
            tree_num = len(tree[i][j])
            while k < tree_num:
                if land[i][j] < tree[i][j][k]:
                    break
                land[i][j] -= tree[i][j][k]
                tree[i][j][k] += 1
                k += 1
            
            for _ in range(k, tree_num):
                total -= 1
                land[i][j] += (tree[i][j].pop() // 2)

def autumn_winter():
    global n, total
    for i in row:
        for j in col:
            for age in tree[i][j]:
                if age % 5 != 0:
                    continue
                for dx, dy in diff:
                    nx, ny = i + dx, j + dy
                    if nx in row and ny in col:
                        total += 1
                        tree[nx][ny].appendleft(1)
            land[i][j] += food[i][j]

for _ in range(k):
    spring_summer()
    autumn_winter()

print(total)
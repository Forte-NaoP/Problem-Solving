import sys

n = int(input())
row = col = range(n)
# 0 = horizon, 1 = vertical, 2 = diagonal
arr = [list(map(int, input().split())) for _ in range(n)]
dist = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
diff = [[(0, 1, 0), (1, 1, 2)], [(1, 0, 1), (1, 1, 2)], [(0, 1, 0), (1, 0, 1), (1, 1, 2)]]

dist[0][1][0] = 1
for i in range(n):
    for j in range(1, n):
        if arr[i][j] == 1:
            continue
        # (i, j) 에서 수평, 수직, 대각방향 확인
        for k in range(3): # k 현재 방향
            for dx, dy, d in diff[k]: # d 도착했을 때 방향
                nx, ny = i + dx, j + dy
                if nx in row and ny in col and arr[nx][ny] != 1:
                    if d == 2 and (arr[nx - 1][ny] == 1 or arr[nx][ny - 1] == 1):
                        continue
                    dist[nx][ny][d] += dist[i][j][k]

print(sum(dist[n - 1][n - 1]))
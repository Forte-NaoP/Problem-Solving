import sys
input = sys.stdin.readline

diff = [(0, 1), (-1, 0), (0, -1), (1, 0)]

n, m, k = map(int, input().split())
row, col = range(n), range(m)
board = [list(input().strip()) for _ in row]

s = list(input().strip())
dp = [[[-1 for _ in range(len(s))] for _ in col] for _ in row]

def recur(x, y, z):
    if dp[x][y][z] != -1:
        return dp[x][y][z]
    
    if z == len(s) - 1:
        dp[x][y][z] = 1
        return dp[x][y][z]
    
    cnt = 0
    for dx, dy in diff:
        nx, ny = x, y
        for _ in range(k):
            nx, ny = nx + dx, ny + dy
            if nx not in row or ny not in col:
                break
            if board[nx][ny] == s[z + 1]:
                cnt += recur(nx, ny, z + 1)

    dp[x][y][z] = cnt
    return dp[x][y][z]

ans = 0
for i in row:
    for j in col:
        if board[i][j] == s[0]:
            ans += recur(i, j, 0)

print(ans)
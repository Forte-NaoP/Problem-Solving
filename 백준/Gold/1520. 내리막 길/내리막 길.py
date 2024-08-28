import sys
input = sys.stdin.readline

def not_in_range(x, y, r, c):
    return x not in r or y not in c

n, m = map(int, input().split())
row, col = range(n), range(m)
diff = [(-1, 0), (0, -1), (1, 0), (0, 1)]
world = [list(map(int, input().split())) for _ in row]
dp = [[-1 for _ in col] for _ in row]

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    cnt = 0
    for dx, dy in diff:
        nx, ny = x + dx, y + dy
        if not_in_range(nx, ny, row, col) or world[nx][ny] >= world[x][y]:
            continue
        cnt += dfs(nx, ny)
    
    dp[x][y] = cnt
    return dp[x][y]

dp[n - 1][m - 1] = 1
print(dfs(0, 0))
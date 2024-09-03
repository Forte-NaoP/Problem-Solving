import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
row, col = range(n), range(m)
board = [list(map(lambda x: 0 if x == 'H' else int(x), input().strip())) for _ in row]
visit = [[False for _ in col] for _ in row]
dp = [[0 for _ in col] for _ in row]
diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# dp[x][y] (x, y)에서 동전을 움직일 수 있는 최대 횟수

def dfs(x, y):
    for dx, dy in diff:
        nx, ny = x + board[x][y] * dx, y + board[x][y] * dy
        if nx not in row or ny not in col or board[nx][ny] == 0:
            continue
        if visit[nx][ny]:
            print(-1)
            exit() 
        if dp[nx][ny] != 0:
            dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
        else:
            visit[nx][ny] = True
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
            visit[nx][ny] = False

    return dp[x][y]
    
visit[0][0] = True
dfs(0, 0)
print(dp[0][0] + 1)
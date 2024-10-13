import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().strip())) for _ in range(n)]
dp = [[0 for _ in range(15)] for _ in range(1 << 15)]

def dfs(visit, cur, price):
    visit |= (1 << cur)    

    if dp[visit][cur] != 0:
        return dp[visit][cur]
    
    for nxt in range(1, n):
        if not (visit & (1 << nxt)) and arr[cur][nxt] >= price:
            dp[visit][cur] = max(dp[visit][cur], dfs(visit, nxt, arr[cur][nxt]) + 1)
    return dp[visit][cur]

print(dfs(0, 0, 0) + 1)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
name = []
for _ in range(n):
    name.append(int(input()))

dp = [sys.maxsize for _ in range(n + 1)]
dp[n - 1] = 0

def recur(x):
    if dp[x] != sys.maxsize:
        return dp[x]
    
    left = m - name[x]
    i = x + 1
    while left >= 0 and i <= n:
        if i == n:
            dp[x] = 0
            break
        dp[x] = min(dp[x], left ** 2 + recur(i))
        left -= name[i] + 1
        i += 1

    return dp[x]

recur(0)
print(dp[0])
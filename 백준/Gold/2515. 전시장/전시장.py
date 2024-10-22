import sys

input = sys.stdin.readline

n, s = map(int, input().split())
dp = [0 for _ in range(n)]
pics = [list(map(int, input().split())) for _ in range(n)]
pics.sort(key=lambda x: x[0])

dp[0] = pics[0][1]
for i in range(1, n):
    low, high = -1, i
    while low + 1 < high:
        mid = (low + high) // 2
        if pics[i][0] - pics[mid][0] >= s:
            low = mid
        else:
            high = mid
    if high == 0:
        dp[i] = max(dp[i - 1], pics[i][1])
    else:
        dp[i] = max(dp[i - 1], dp[high - 1] + pics[i][1])

print(dp[-1])
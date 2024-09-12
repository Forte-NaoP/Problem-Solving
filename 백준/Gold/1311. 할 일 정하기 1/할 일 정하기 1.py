import sys
from collections import defaultdict

input = sys.stdin.readline

INF = 999_999
n = int(input())
job = [list(map(int, input().split())) for _ in range(n)]
dp = [[INF for _ in range(1 << n)] for _ in range(n)]

def recur(idx, state):
    if state == (1 << n) - 1:
        return 0
    if dp[idx][state] != 999_999:
        return dp[idx][state]

    for i in range(n):
        if state & (1 << i):
            continue
        dp[idx][state] = min(dp[idx][state], recur(idx + 1, state | (1 << i)) + job[idx][i])

    return dp[idx][state]

print(recur(0, 0))
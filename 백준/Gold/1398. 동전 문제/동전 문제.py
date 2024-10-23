import sys
import math

input = sys.stdin.readline

dp = {0: 0}

def nearest(x):
    k = int(math.log10(x))
    p10 = 10 ** k
    k_ = k // 2
    while (p25 := 25 * 100 ** k_) > x:
        k_ -= 1
    if k_ < 0:
        p25 = 1
    return p10, p25

def recur(x):
    if x in dp.keys():
        return dp[x]
    p10, p25 = nearest(x)
    dp[x] = min(recur(x - p10) + 1, recur(x - p25) + 1)
    return dp[x]

for _ in range(int(input())):
    x = int(input())
    print(recur(x))

import sys
from math import comb

input = lambda : sys.stdin.readline().strip()
MOD = 10_007
n = int(input())
ans = 0
cnt, sign = 1, 1
while n >= 4:
    ans += sign * comb(13, cnt) * comb(52 - (cnt << 2), n - 4)
    cnt += 1
    sign = -sign
    n -= 4
print(ans % MOD)

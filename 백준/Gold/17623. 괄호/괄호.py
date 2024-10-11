import sys

input = sys.stdin.readline

table = {1: '(', 2: ')', 3: '{', 4: '}', 5: '[', 6: ']'}
def convert(x):
    res = []
    while x > 0:
        res.append(table[x % 10])
        x //= 10
    res.reverse()
    return ''.join(res)

dp = [[float('inf'), 1] for _ in range(1001)]
dp[0][:] = 0, 0
dp[1][:] = 12, 2
dp[2][:] = 34, 2
dp[3][:] = 56, 2

d = lambda x, y: (10 ** (y + 1) + x * 10 + 2, y + 2)
e = lambda x, y: (3 * 10 ** (y + 1) + x * 10 + 4, y + 2)
f = lambda x, y: (5 * 10 ** (y + 1) + x * 10 + 6, y + 2)

for i in range(4, 1001):
    if i % 2 == 0:
        dmap = d(*dp[i // 2])
        if dmap[0] < dp[i][0]:
            dp[i][:] = dmap
    if i % 3 == 0:
        dmap = e(*dp[i // 3])
        if dmap[0] < dp[i][0]:
            dp[i][:] = dmap
    if i % 5 == 0:
        dmap = f(*dp[i // 5])
        if dmap[0] < dp[i][0]:
            dp[i][:] = dmap
    for j in range(1, i // 2 + 1):
        dmap = min(
            dp[i - j][0] * 10 ** dp[j][1] + dp[j][0],
            dp[j][0] * 10 ** dp[i - j][1] + dp[i - j][0]
        )
        digit = dp[i - j][1] + dp[j][1]
        if dmap < dp[i][0]:
            dp[i][:] = dmap, digit

for _ in range(int(input())):
    print(convert(dp[int(input())][0]))


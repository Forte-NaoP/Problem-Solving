import sys

input = sys.stdin.readline

def convert(x):
    res = []
    table = {1: '(', 2: ')', 3: '{', 4: '}', 5: '[', 6: ']'}
    while x > 0:
        res.append(table[x % 10])
        x //= 10
    res.reverse()
    return ''.join(res)

dp = [[float('inf'), 1] for _ in range(1001)]
dp[0][:] = 0, 0

a = lambda x, y: (min(12 * 10 ** y + x, 100 * x + 12), y + 2)
b = lambda x, y: (min(34 * 10 ** y + x, 100 * x + 34), y + 2)
c = lambda x, y: (min(56 * 10 ** y + x, 100 * x + 56), y + 2)
d = lambda x, y: (10 ** (y + 1) + x * 10 + 2, y + 2)
e = lambda x, y: (3 * 10 ** (y + 1) + x * 10 + 4, y + 2)
f = lambda x, y: (5 * 10 ** (y + 1) + x * 10 + 6, y + 2)

for i in range(1, 1001):
    if i >= 1:
        dmap = a(*dp[i - 1])
        if dmap[0] < dp[i][0]:
            dp[i][:] = dmap
    if i >= 2:
        dmap = b(*dp[i - 2])
        if dmap[0] < dp[i][0]:
            dp[i][:] = dmap
    if i >= 3:
        dmap = c(*dp[i - 3])
        if dmap[0] < dp[i][0]:
            dp[i][:] = dmap
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

for _ in range(int(input())):
    print(convert(dp[int(input())][0]))

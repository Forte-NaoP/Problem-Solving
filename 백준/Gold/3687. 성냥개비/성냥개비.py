import sys

input = sys.stdin.readline

table = [0, 0, 1, 7, 4, 2, 0, 8]
dp = [float('inf') for _ in range(101)]
for i in range(2, 8):
    dp[i] = table[i]
dp[6] = 6

for i in range(8, 101):
    for j in range(2, 8):
        dp[i] = min(dp[i], dp[i - j] * 10 + table[j])

for _ in range(int(input())):
    n = int(input())
    if n % 2:
        M = '7' + '1' * ((n - 3) // 2)
    else:
        M = '1' * (n // 2)
    print(dp[n], int(M))
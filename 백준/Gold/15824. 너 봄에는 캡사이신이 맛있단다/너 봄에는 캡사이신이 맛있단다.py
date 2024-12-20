import sys

input = lambda : sys.stdin.readline().strip()
MOD = 1_000_000_007
n = int(input())
hot = sorted(list(map(int, input().split())))
pow2 = [1 for _ in range(n)]
for i in range(1, n):
    pow2[i] = (pow2[i - 1] * 2) % MOD

ans = 0
for i in range(n):
    ans -= hot[i] * pow2[n - 1 - i] % MOD
    ans += hot[i] * pow2[i] % MOD
    ans %= MOD

print(ans)
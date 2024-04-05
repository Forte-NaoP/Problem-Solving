import sys

a, b, c = map(int, input().split())
pow_a = [a]
x = a
for _ in range(32):
    pow_a.append((pow_a[-1] ** 2) % c)

i = 0
ans = 1
while b > 0:
    if b % 2:
        ans = (ans * pow_a[i]) % c
    i += 1
    b >>= 1
    
print(ans)
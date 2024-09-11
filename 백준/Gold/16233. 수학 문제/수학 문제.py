import sys

input = sys.stdin.readline

t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    if n % 9 != 0:
        ans.append(-1)
        continue
    
    mod = 999_999_999
    x = 0
    while mod > 0:
        if n // mod > 9:
            break
        x = (x + n // mod) * 10
        n %= mod
        mod //= 10

    if n != 0:
        ans.append(-1)
    else:
        ans.append(x)
        
print(' '.join(map(str, ans)))
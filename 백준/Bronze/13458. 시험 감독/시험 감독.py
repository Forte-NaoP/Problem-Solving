import sys

input = sys.stdin.readline

n = int(input())
test = list(map(int, input().split()))
b, c = map(int, input().split())
ans = 0

for t in test:
    ans += 1
    t -= b
    if t > 0:
        ans += (t // c)
        if t % c != 0:
            ans += 1

print(ans)

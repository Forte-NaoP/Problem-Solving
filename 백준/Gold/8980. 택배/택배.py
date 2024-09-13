import sys

input = sys.stdin.readline

n, max_cap = map(int, input().split())
m = int(input())

info = []
for _ in range(m):
    a, b, c = map(int, input().split())
    info.append((a, b, c))
info.sort(key=lambda x: (x[1], x[0]))

ans = 0
truck = [0 for _ in range(n + 1)]
cap = 0
last = 0

for a, b, c in info:
    for i in range(last, a + 1):
        ans += truck[i]
        cap -= truck[i]
        truck[i] = 0
    last = a
    if cap == max_cap:
        continue
    truck[b] += min(max_cap - cap, c)
    cap += min(max_cap - cap, c)

ans += sum(truck)

print(ans)
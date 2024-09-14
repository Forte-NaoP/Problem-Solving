import sys

input = sys.stdin.readline

w, n = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()
pack = [[] for _ in range(w + 1)]

for i in range(n):
    for j in range(i + 1, n):
        ij = weight[i] + weight[j]
        if ij > w:
            continue
        pack[ij] = (i, j)

for i in range(n):
    for j in range(i + 1, n):
        ij = weight[i] + weight[j]
        if ij > w:
            continue
        kl = w - ij
        if pack[kl] and i not in pack[kl] and j not in pack[kl]:
            print('YES')
            exit()
print('NO')
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n, m, k = map(int, input().split())
parent = list(map(lambda x: -int(x), input().split()))
group = [1 for _ in range(n)]

def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    
    if parent[x] < parent[y]:
        x, y = y, x
    
    parent[y] += parent[x]
    group[y] += group[x]
    parent[x] = y

    return True

for _ in range(m):
    a, b = map(int, input().split())
    union(a - 1, b - 1)

item = []
chk = [False for _ in range(n)]
for i in range(n):
    pi = find(i)
    if not chk[pi] and parent[pi] < 0:
        item.append((group[pi], -parent[pi]))
        chk[pi] = True

dp = [0 for _ in range(k)]
for i in range(len(item)):
    w, v = item[i]
    for j in range(k - 1, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[-1])

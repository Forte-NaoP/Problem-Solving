import sys

input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])
parent = [i for i in range(n + 1)]
rank = [0 for _ in range(n + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False

    if rank[x] > rank[y]:
        x, y = y, x

    parent[x] = y
    if rank[x] == rank[y]:
        rank[y] += 1

    return True

streak = 1
for a, b, c in edges:
    if union(a, b) and streak == c:
        streak += 1
    else:
        break
print(streak)
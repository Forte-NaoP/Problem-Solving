import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
tree = defaultdict(list)
parent = [[0 for _ in range(18)] for _ in range(n + 1)]
depth = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def init(x, p):
    depth[x] = depth[p] + 1
    parent[x][0] = p

    for i in range(1, 18):
        parent[x][i] = parent[parent[x][i - 1]][i - 1]

    for nxt in tree[x]:
        if nxt == p:
            continue
        init(nxt, x)

init(1, 0)

def lca(a, b):
    if a == 1 or b == 1:
        return 1
    if depth[a] < depth[b]:
        a, b = b, a
    
    if depth[a] != depth[b]:
        for i in range(17, -1, -1):
            if depth[parent[a][i]] >= depth[b]:
                a = parent[a][i]

    ret = b
    if a != b:
        for i in range(17, -1, -1):
            if parent[a][i] != parent[b][i]:
                a = parent[a][i]
                b = parent[b][i]
            ret = parent[b][i]
    return ret
        

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))

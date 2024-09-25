import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = defaultdict(list)
depth = [0 for _ in range(n + 1)]
max_depth = 17
parent = [[0 for _ in range(max_depth + 1)] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def init(cur, p):
    depth[cur] = depth[p] + 1
    parent[cur][0] = p

    for i in range(1, max_depth + 1):
        parent[cur][i] = parent[parent[cur][i - 1]][i - 1]

    for nxt in tree[cur]:
        if nxt == p:
            continue
        init(nxt, cur)

def query(a, b):
    if a == 1 or b == 1:
        return 1
    
    if depth[a] > depth[b]:
        a, b = b, a

    if depth[a] != depth[b]:
        for i in range(max_depth, -1, -1):
            if depth[parent[b][i]] >= depth[a]:
                b = parent[b][i]
    
    lca = a
    if a != b:
        for i in range(max_depth, -1, -1):
            if parent[a][i] != parent[b][i]:
                a = parent[a][i]
                b = parent[b][i]
            lca = parent[a][i]

    return lca

init(1, 0)
for _ in range(int(input())):
    r, u, v = map(int, input().split())
    uv = query(u, v)
    ru = query(r, u)
    rv = query(r, v)

    if ru == rv:
        print(uv)
    else:
        if ru != uv:
            print(ru)
        else:
            print(rv)
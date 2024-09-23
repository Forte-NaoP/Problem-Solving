import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

max_depth = 17
n = int(input())
tree = defaultdict(lambda: defaultdict(int))
parent = [[0 for _ in range(max_depth + 1)] for _ in range(n + 1)]
road = [[[0, 0] for _ in range(max_depth + 1)] for _ in range(n + 1)]
depth = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a][b] = c
    tree[b][a] = c

def init(cur, p):
    depth[cur] = depth[p] + 1
    parent[cur][0] = p
    road[cur][0][0] = road[cur][0][1] = tree[p][cur]

    for i in range(1, max_depth + 1):
        past_parent = parent[cur][i - 1]
        parent[cur][i] = parent[past_parent][i - 1]
        road[cur][i][0] = min(road[past_parent][i - 1][0], road[cur][i - 1][0])
        road[cur][i][1] = max(road[past_parent][i - 1][1], road[cur][i - 1][1])
    
    for nxt in tree[cur].keys():
        if nxt == p:
            continue
        init(nxt, cur)

def lca_query(a, b):
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

def road_query(lca, a):
    md, Md = 10 ** 9, 0

    for i in range(max_depth, -1, -1):
        if depth[parent[a][i]] >= depth[lca]:
            md = min(md, road[a][i][0])
            Md = max(Md, road[a][i][1])
            a = parent[a][i]

    return md, Md

init(1, 0)
for _ in range(int(input())):
    a, b = map(int, input().split())
    lca = lca_query(a, b)
    m, M = 10 ** 9, 0
    if lca != a:
        ma, Ma = road_query(lca, a)
        m = min(ma, m)
        M = max(Ma, M)
    if lca != b:
        mb, Mb = road_query(lca, b)
        m = min(mb, m)
        M = max(Mb, M)
    print(m, M)

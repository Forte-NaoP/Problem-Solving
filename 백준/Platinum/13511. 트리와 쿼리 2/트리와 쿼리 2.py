import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

max_depth = 17
n = int(input())
tree = defaultdict(lambda: defaultdict(int))
parent = [[0 for _ in range(max_depth + 1)] for _ in range(n + 1)]
dist = [0 for _ in range(n + 1)]
depth = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a][b] = c
    tree[b][a] = c

def init(cur, p):
    depth[cur] = depth[p] + 1
    parent[cur][0] = p
    dist[cur] = dist[p] + tree[p][cur]

    for i in range(1, max_depth + 1):
        parent[cur][i] = parent[parent[cur][i - 1]][i - 1]
    
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

def kth_node(a, b, k):
    k -= 1
    lca = lca_query(a, b)
    a_len = depth[a] - depth[lca]
    b_len = depth[b] - depth[lca]

    if a_len < k:
        k = a_len + b_len - k
        a, b = b, a
    
    if k == 0:
        return a
    
    kth = 0
    for i in range(max_depth, -1, -1):
        if (1 << i) <= k:
            k -= (1 << i)
            a = parent[a][i]
            kth = a
        if k == 0:
            break

    return kth

init(1, 0)
for _ in range(int(input())):
    q, *p = map(int, input().split())
    if q == 1:
        a, b = p
        lca = lca_query(a, b)
        print(dist[a] + dist[b] - 2 * dist[lca])
    else:
        print(kth_node(*p))

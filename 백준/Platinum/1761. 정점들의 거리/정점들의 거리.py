import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

max_depth = 16
n = int(input())
parent = [[0 for _ in range(max_depth + 1)] for _ in range(n + 1)]
dist = [0 for _ in range(n + 1)]
depth = [-1 for _ in range(n + 1)]
tree = defaultdict(dict)
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a][b] = c
    tree[b][a] = c

def make_tree(cur, p):
    depth[cur] = depth[p] + 1
    parent[cur][0] = p
    if cur != 1:
        dist[cur] = dist[p] + tree[p][cur]

    for i in range(1, max_depth + 1):
        parent[cur][i] = parent[parent[cur][i - 1]][i - 1]

    for nxt in tree[cur].keys():
        if nxt == p:
            continue
        make_tree(nxt, cur)

def query(low, high):
    if depth[low] > depth[high]:
        low, high = high, low

    if depth[low] != depth[high]:
        for i in range(max_depth, -1, -1):
            if depth[parent[high][i]] >= depth[low]:
                high = parent[high][i]
    lca = low
    if low != high:
        for i in range(max_depth, -1, -1):
            if parent[low][i] != parent[high][i]:
                low = parent[low][i]
                high = parent[high][i]
            lca = parent[low][i]
    return lca

make_tree(1, 0)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    lca = query(a, b)
    print(dist[a] + dist[b] - 2 * dist[lca])
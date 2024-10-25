import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
ant = [0] + [int(input()) for _ in range(n)]
tree = defaultdict(dict)
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a][b] = c
    tree[b][a] = c

max_depth = 17
parent = [[[0, 0] for _ in range(max_depth)] for _ in range(n + 1)]
def init(cur, p):
    parent[cur][0][0] = p
    parent[cur][0][1] = tree[cur][p] if p != 0 else 0

    for i in range(1, max_depth):
        ith_parent, ith_cost = parent[cur][i - 1]
        parent[cur][i][0] = parent[ith_parent][i - 1][0]
        parent[cur][i][1] = parent[ith_parent][i - 1][1] + ith_cost
    
    for nxt in tree[cur].keys():
        if nxt == p:
            continue
        init(nxt, cur)

init(1, 0)

for i in range(1, n + 1):
    cur = i
    energy = ant[i]
    for j in range(max_depth - 1, -1, -1):
        if parent[cur][j][0] != 0 and energy >= parent[cur][j][1]:
            energy -= parent[cur][j][1]
            cur = parent[cur][j][0]
    print(cur)
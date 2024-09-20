import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
city = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    city[a].append(b)
    city[b].append(a)

max_h = 15
parent = [[0 for _ in range(max_h + 1)] for _ in range(n + 1)]
depth = [0 for _ in range(n + 1)]

def init(cur, p):
    depth[cur] = depth[p] + 1

    parent[cur][0] = p
    for i in range(1, max_h + 1):
        parent[cur][i] = parent[parent[cur][i - 1]][i - 1]
    
    for nxt in city[cur]:
        if nxt == p:
            continue
        init(nxt, cur)
    
def query(a, b):
    if a == 1 or b == 1:
        return 1
    
    if depth[a] > depth[b]:
        a, b, = b, a

    if depth[a] != depth[b]:
        for i in range(max_h, -1, -1):
            if depth[parent[b][i]] >= depth[a]:
                b = parent[b][i]
    
    lca = a
    if a != b:
        for i in range(max_h, -1, -1):
            if parent[a][i] != parent[b][i]:
                a = parent[a][i]
                b = parent[b][i]
            lca = parent[a][i]
    
    return lca

init(1, 0)
m = int(input())
st = 1
ans = 0
for _ in range(m):
    ed = int(input())
    lca = query(st, ed)
    ans += depth[st] + depth[ed] - 2 * depth[lca]
    st = ed

print(ans)

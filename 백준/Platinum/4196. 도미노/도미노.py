import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def tarzan(g, n):

    _label = 0
    label = [0 for _ in range(n + 1)]
    finished = [0 for _ in range(n + 1)]
    st = []
    scc_top = []

    def _tarzan(u):
        nonlocal _label

        _label += 1
        parent = label[u] = _label
        st.append(u)

        for v in g[u]:
            if label[v] == 0:
                parent = min(parent, _tarzan(v))
            elif finished[v] == 0:
                parent = min(parent, label[v])
        
        if parent == label[u]:
            while True:
                p = st.pop()
                finished[p] = u
                if p == u:
                    scc_top.append(p)
                    break
        return parent
    
    for i in range(1, n + 1):
        if label[i] == 0:
            _tarzan(i)

    indegree = defaultdict(int)
    for u in g.keys():
        for v in g[u]:
            if finished[u] != finished[v]:
                indegree[finished[v]] += 1
    ans = 0
    for top in scc_top:
        if indegree[top] == 0:
            ans += 1
    return ans

for _ in range(int(input())):
    n, m = map(int, input().split())
    g = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
    print(tarzan(g, n))
import sys
from collections import defaultdict

sys.setrecursionlimit(10**5)
input = lambda : sys.stdin.readline().strip()

def tarzan(g, n):
    _label = 0
    label = [0 for _ in range(n + 1)]
    finished = [0 for _ in range(n + 1)]
    st = []
    scc_set = {}
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
            scc = []
            while True:
                p = st.pop()
                finished[p] = u
                scc.append(p)
                if p == u:
                    scc_top.append(u)
                    scc_set[u] = scc
                    break
        return parent
    
    for i in range(1, n + 1):
        if label[i] == 0:
            _tarzan(i)

    outdegree = defaultdict(int)
    for u in g.keys():
        for v in g[u]:
            if finished[u] != finished[v]:
                outdegree[finished[u]] += 1

    ans = []
    for top in scc_top:
        if outdegree[top] == 0:
            ans.extend(scc_set[top])
    ans.sort()
    print(' '.join(map(str, ans)))


while (line := input()) != '0':
    n, m = map(int, line.split())
    g = defaultdict(list)
    e = map(int, input().split())
    for i in range(m):
        g[next(e)].append(next(e))
    tarzan(g, n)
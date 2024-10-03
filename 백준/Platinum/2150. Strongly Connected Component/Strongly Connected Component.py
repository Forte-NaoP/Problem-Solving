import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def tarzan(g, n):

    _label = 0
    label = [0 for _ in range(n + 1)]
    finished = [False for _ in range(n + 1)]
    st = []
    scc = []

    def _tarzan(u):
        nonlocal _label

        _label += 1
        parent = label[u] = _label
        st.append(u)

        for v in g[u]:
            if label[v] == 0:
                parent = min(parent, _tarzan(v))
            elif not finished[v]:
                parent = min(parent, label[v])
        
        if parent == label[u]:
            scc_set = []
            while True:
                p = st.pop()
                scc_set.append(p)
                finished[p] = True
                if p == u:
                    break
            scc_set.sort()
            scc_set.append(-1)
            scc.append(scc_set)
        
        return parent
    
    for i in range(1, n + 1):
        if label[i] == 0:
            _tarzan(i)
    scc.sort(key=lambda x: x[0])
    return scc

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)

scc = tarzan(g, n)
print(len(scc))
for scc_set in scc:
    print(*scc_set)
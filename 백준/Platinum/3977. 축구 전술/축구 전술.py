import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def tarzan(g, n):
    INF = 10 ** 9
    _label = 0
    label = [0 for _ in range(n)]
    finished = [INF for _ in range(n)]
    st = []
    scc_set = []

    def _tarzan(u):
        nonlocal _label
        _label += 1
        parent = label[u] = _label
        st.append(u)

        for v in g[u]:
            if label[v] == 0:
                parent = min(parent, _tarzan(v))
            elif finished[v] == INF:
                parent = min(parent, label[v])

        if parent == label[u]:
            scc_set.append([])
            while True:
                p = st.pop()
                finished[p] = len(scc_set) - 1
                scc_set[-1].append(p)
                if p == u:
                    break
        return parent
    
    for u in range(n):
        if label[u] == 0:
            _tarzan(u)

    indegree = defaultdict(int)
    for u in g.keys():
        for v in g[u]:
            if finished[u] != finished[v]:
                indegree[finished[v]] += 1

    start = cnt = 0
    for scc_id in range(len(scc_set)):
        if indegree[scc_id] == 0:
            start = scc_id
            cnt += 1

    if cnt > 1:
        print('Confused')
    else:
        if cnt == 0:
            for i in range(n):
                print(i)
        else:
            scc_set[start].sort()
            for i in scc_set[start]:
                print(i)
    print()

for _ in range(int(input())):
    g = defaultdict(list)
    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
    tarzan(g, n)
    input()

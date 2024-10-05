import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def convert(x):
    u = (abs(x) - 1) * 2
    _u = u + 1
    if x < 0:
        u, _u = _u, u
    return u, _u

def sat_2(g, n):
    _label = 0
    label = [0 for _ in range(n)]
    finished = [-1 for _ in range(n)]
    st = []

    def _tarzan(u):
        nonlocal _label
        _label += 1
        parent = label[u] = _label
        st.append(u)

        for v in g[u]:
            if label[v] == 0:
                parent = min(parent, _tarzan(v))
            elif finished[v] == -1:
                parent = min(parent, label[v])

        if parent == label[u]:
            while True:
                p = st.pop()
                finished[p] = label[u]
                if p == u:
                    break
        return parent
    
    for u in range(0, n, 2):
        if label[u] == 0:
            _tarzan(u)

    for u in range(0, n, 2):
        if finished[u] == finished[u + 1]:
            return 0
    return 1

g = defaultdict(list)
n, m = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    u, _u = convert(a)
    v, _v = convert(b)
    g[_u].append(v)
    g[_v].append(u)

print(sat_2(g, n * 2))
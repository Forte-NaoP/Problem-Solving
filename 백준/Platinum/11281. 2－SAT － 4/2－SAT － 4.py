import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n, m = map(int, input().split())

def neg(x):
    if x < n:
        return x + n
    return x - n

def sat_2(g, n):
    INF = 10 ** 9
    _label = 0
    label = [0 for _ in range(n + 1)]
    finished = [INF for _ in range(n + 1)]
    st = []
    ans = [0 for _ in range(n // 2)]
    scc_id = 0

    def _tarzan(u):
        nonlocal _label, scc_id
        _label += 1
        parent = label[u] = _label
        st.append(u)

        for v in g[u]:
            if label[v] == 0:
                parent = min(parent, _tarzan(v))
            elif finished[v] == INF:
                parent = min(parent, label[v])

        if parent == label[u]:
            scc_id += 1
            while True:
                p = st.pop()
                finished[p] = scc_id
                if p == u:
                    break
        return parent
    
    for u in range(n):
        if label[u] == 0:
            _tarzan(u)

    for u in range(n // 2):
        if finished[u] == finished[neg(u)]:
            return 0, []
        elif finished[u] < finished[neg(u)]:
            ans[u] = 1
    return 1, ans

g = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    a = -a - 1 + n if a < 0 else a - 1
    b = -b - 1 + n if b < 0 else b - 1
    g[neg(a)].append(b)
    g[neg(b)].append(a)

p, ans = sat_2(g, n * 2)
print(p)
print(*ans)
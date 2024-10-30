import sys
sys.setrecursionlimit(10 ** 5)

input = lambda : sys.stdin.readline().strip()

def tarzan(g, n):
    _label = 0
    label = [0 for _ in range(n + 1)]
    finished = [0 for _ in range(n + 1)]
    st = []

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
        
        if label[u] == parent:
            while True:
                p = st.pop()
                finished[p] = u
                if p == u:
                    break
 
        return parent
    
    for i in range(1, n + 1):
        if label[i] == 0:
            _tarzan(i)

    for i in range(1, n // 2 + 1):
        if finished[i] == finished[-i]:
            return 0
    return 1

while True:
    m, n = map(int, input().split())
    if (m, n) == (0, 0):
        break
    g = [[] for _ in range(n * 2 + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[-a].append(b)
        g[-b].append(a)
    print(tarzan(g, n * 2))

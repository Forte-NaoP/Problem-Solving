import sys
sys.setrecursionlimit(10**5)
input = lambda : sys.stdin.readline().strip()

def tarzan(g, n):
    _label = 0
    label = [-1 for _ in range(n + 1)]
    bridge = []

    def _tarzan(u, p):
        nonlocal _label
        _label += 1
        parent = label[u] = _label

        for v in g[u]:
            if v == p:
                continue
            if label[v] == -1:
                nxt = _tarzan(v, u)
                parent = min(parent, nxt)
                if nxt > label[u]:
                    bridge.append((min(u, v), max(u, v)))
            else:
                parent = min(parent, label[v])

        return parent
    
    for u in range(1, n + 1):
        if label[u] == -1:
            _tarzan(u, -1)

    return bridge   

v, e = map(int, input().split())
g = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

bridge = tarzan(g, v)
bridge.sort()
buf = f'{len(bridge)}\n'
buf += '\n'.join(map(lambda x: f'{x[0]} {x[1]}', bridge))
print(buf)

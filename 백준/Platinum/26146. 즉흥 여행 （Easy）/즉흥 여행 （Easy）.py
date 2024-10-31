import sys
from typing import List, Dict

input = lambda : sys.stdin.readline().strip()

def tarzan(g: List[List[int]], n: int):
    _label = 0
    label = [0 for _ in range(n + 1)]
    finished = [0 for _ in range(n + 1)]
    stack = []

    def _tarzan(u):
        nonlocal _label
        _label += 1
        parent = label[u] = _label
        stack.append(u)

        for v in g[u]:
            if label[v] == 0:
                parent = min(parent, _tarzan(v))
            elif finished[v] == 0:
                parent = min(parent, label[v])
        
        if label[u] == parent:
            while True:
                p = stack.pop()
                finished[p] = u
                if u == p:
                    break
        
        return parent

    for i in range(1, n + 1):
        if label[i] == 0:
            _tarzan(i)

    return all(x == finished[1] for x in finished[1:])

n, m = map(int, input().split())
sys.setrecursionlimit(3 * 10 ** 5)
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)

print('Yes' if tarzan(g, n) else 'No')
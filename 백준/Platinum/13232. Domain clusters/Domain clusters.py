import sys
from typing import List

input = lambda : sys.stdin.readline().strip()
sys.setrecursionlimit(10**4)

def tarzan(g: List[List[str]], n: int) -> int:
    _label = 0
    label = [-1 for _ in range(n + 1)]
    finished = [-1 for _ in range(n + 1)]
    stack = []
    max_size = 0

    def _tarzan(u: int) -> int:
        nonlocal _label, max_size
        _label += 1
        parent = label[u] = _label
        stack.append(u)

        for v in g[u]:
            if label[v] == -1:
                parent = min(parent, _tarzan(v))
            elif finished[v] == -1:
                parent = min(parent, label[v])
        
        if parent == label[u]:
            scc_size = 0
            while True:
                p = stack.pop()
                finished[p] = u
                scc_size += 1
                if p == u:
                    max_size = max(scc_size, max_size)
                    break
        return parent
    
    for i in range(1, n + 1):
        if label[i] == -1:
            _tarzan(i)

    return max_size

n, m = int(input()), int(input())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
print(tarzan(g, n))

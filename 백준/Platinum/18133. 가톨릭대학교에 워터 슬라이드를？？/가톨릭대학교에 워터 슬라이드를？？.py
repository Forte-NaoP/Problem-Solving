import sys
from typing import List, Dict
from collections import defaultdict

input = lambda : sys.stdin.readline().strip()

def tarzan(g: List[List[str]], n: int) -> int:
    _label = 0
    label = [-1 for _ in range(n + 1)]
    finished = [-1 for _ in range(n + 1)]
    stack = []
    scc_top = []

    def _tarzan(u):
        nonlocal _label
        _label += 1
        parent = label[u] = _label
        stack.append(u)

        for v in g[u]:
            if label[v] == -1:
                parent = min(parent, _tarzan(v))
            elif finished[v] == -1:
                parent = min(parent, label[v])
        
        if parent == label[u]:
            while True:
                p = stack.pop()
                finished[p] = u
                if p == u:
                    scc_top.append(u)
                    break
        return parent
    
    for i in range(1, n + 1):
        if label[i] == -1:
            _tarzan(i)

    indegree = defaultdict(int)
    for u in range(1, n + 1):
        for v in g[u]:
            if finished[u] != finished[v]:
                indegree[finished[v]] += 1
    ans = 0
    for i in scc_top:
        if indegree[i] == 0:
            ans += 1

    return ans

sys.setrecursionlimit(100_100)
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
print(tarzan(g, n))
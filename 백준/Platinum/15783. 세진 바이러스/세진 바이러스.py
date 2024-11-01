import sys
from typing import List
from collections import defaultdict

input = lambda : sys.stdin.readline().strip()

def tarzan(g: List[List[int]], n: int) -> bool:
    _label = 0
    label = [-1 for _ in range(n)]
    finished = [-1 for _ in range(n)]
    scc_top = []
    stack = []

    def _tarzan(u):
        nonlocal _label
        _label += 1
        parent = label[u] = _label
        stack.append(u)

        for v in g[u]:
            if label[v] == -1:
                parent = min(_tarzan(v), parent)
            elif finished[v] == -1:
                parent = min(label[v], parent)
        
        if label[u] == parent:
            while True:
                p = stack.pop()
                finished[p] = u
                if p == u:
                    scc_top.append(u)
                    break
        return parent
    
    for i in range(n):
        if label[i] == -1:
            _tarzan(i)

    indegree = defaultdict(int)
    for u in range(n):
        for v in g[u]:
            if finished[u] != finished[v]:
                indegree[finished[v]] += 1
    
    ans = 0
    for u in scc_top:
        if indegree[u] == 0:
            ans += 1
    return ans


sys.setrecursionlimit(10 ** 5)
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)

print(tarzan(g, n))

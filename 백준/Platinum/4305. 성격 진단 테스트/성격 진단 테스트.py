import sys
from typing import List

input = lambda : sys.stdin.readline().strip()

def tarzan(g: List[List[str]], choice):
    _label = 0
    label = [-1 for _ in range(26)]
    finished = [-1 for _ in range(26)]
    stack = []
    scc_set = []

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
            scc = []
            while True:
                p = stack.pop()
                finished[p] = u
                scc.append(chr(p + ord('A')))
                if p == u:
                    scc.sort()
                    scc_set.append(' '.join(scc))
                    break
        return parent
    
    for c in range(26):
        if choice[c] > 0 and label[c] == -1:
            _tarzan(c)

    scc_set.sort()
    return scc_set


while (n := int(input())) != 0:
    g = [[] for _ in range(26)]
    choice = [0 for _ in range(26)]
    for _ in range(n):
        q = list(map(lambda x: ord(x) - ord('A'), input().split()))
        q, pick = q[:-1], q[-1]
        for c in q:
            choice[c] += 1
            if c != pick:
                g[pick].append(c)
    for scc in tarzan(g, choice):
        print(scc)
    print()

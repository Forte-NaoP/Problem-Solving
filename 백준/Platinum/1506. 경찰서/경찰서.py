import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
cost = list(map(int, input().split()))
city = defaultdict(list)
for i in range(n):
    for j, v in enumerate(input().strip()):
        if v == '1':
            city[i].append(j)

def tarzan():
    global n

    label = [0 for _ in range(n)]
    finished = [False for _ in range(n)]
    _label = 0
    st = []
    scc_set = []

    def _tarzan(u):
        nonlocal _label

        _label += 1
        parent = label[u] = _label
        st.append(u)

        for v in city[u]:
            if label[v] == 0:
                parent = min(parent, _tarzan(v))
            elif not finished[v]:
                parent = min(parent, label[v])

        if parent == label[u]:
            scc = []
            while True:
                p = st.pop()
                finished[p] = True
                scc.append(p)
                if p == u:
                    break
            scc_set.append(scc)
        
        return parent
    
    for i in range(n):
        if label[i] == 0:
            _tarzan(i)

    return scc_set

ans = 0
scc_set = tarzan()
for scc in scc_set:
    ans += min(map(lambda x: cost[x], scc))
print(ans)
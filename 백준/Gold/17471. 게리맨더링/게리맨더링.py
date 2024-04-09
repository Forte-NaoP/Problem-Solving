import sys
from collections import deque, defaultdict
from itertools import combinations

n = int(input())
city = [i for i in range(n)]
population = list(map(int, input().split()))
total = sum(population)

graph = defaultdict(dict)
for i in range(n):
    info = list(map(lambda x: int(x) - 1, input().split()))
    for j in info[1:]:
        graph[i][j] = True
        graph[j][i] = True

q = deque()
def bfs(group):
    visit = set()
    visit.add(group[0])
    q.append(group[0])

    while q:
        x = q.popleft()

        for nxt in graph[x]:
            if nxt not in group or nxt in visit:
                continue
            q.append(nxt)
            visit.add(nxt)

    if len(visit) == len(group):
        return True
    else:
        return False
    

ans = 99999
for i in range(1, n // 2 + 1):
    comb = list(combinations(city, i))
    for g1 in comb:
        g2 = [c for c in city if c not in g1]
        g1_p = sum(map(lambda x: population[x], g1))
        g2_p = total - g1_p

        if bfs(g1) and bfs(g2):
            ans = min(abs(g1_p - g2_p), ans)

if ans == 99999:
    ans = -1
print(ans)
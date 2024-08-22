import sys
from copy import deepcopy
from collections import deque, defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    build_time = [0] + list(map(int, input().split()))
    graph = defaultdict(list)
    indegree = [0] * (n + 1)

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    graph[0] = [i for i in range(1, n + 1)]

    final_build = int(input())

    st = deque(filter(lambda x: indegree[x] == 0, range(1, n + 1)))
    spend_time = defaultdict(int)

    while st:
        cur = st.popleft()

        if cur == final_build:
            break

        if cur in graph:
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                spend_time[nxt] = max(spend_time[nxt], spend_time[cur] + build_time[cur])
                if indegree[nxt] == 0:
                    st.append(nxt)
    
    print(spend_time[final_build] + build_time[final_build])
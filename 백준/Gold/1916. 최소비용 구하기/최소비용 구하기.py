import sys
import heapq

input = sys.stdin.readline
hpush = heapq.heappush
hpop = heapq.heappop

n = int(input())
m = int(input())

q = []
bus = [[] for _ in range(n+1)]
dist = [2147483647] * (n+1)

for _ in range(m):
    s, t, d = map(int, input().split(' '))
    bus[s].append((d, t))

s, t = map(int, input().split(' '))
dist[s] = 0
hpush(q, (0, s))

while len(q) != 0:
    cur_dist, cur = hpop(q)

    if cur_dist > dist[cur]:
        continue

    for nxt_dist, nxt in bus[cur]:
        nxt_dist = nxt_dist + cur_dist
        if nxt_dist < dist[nxt]:
            hpush(q, (nxt_dist, nxt))
            dist[nxt] = nxt_dist

print(dist[t])

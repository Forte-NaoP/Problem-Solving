import sys
from collections import defaultdict
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = lambda : sys.stdin.readline().strip()

def height(x):
    return ord(x) - ord('A') if x <= 'Z' else ord(x) - ord('a') + 26

INF = 1e9
n, m, limit, dawn = map(int, input().split())
mt = [list(map(lambda x: height(x), input())) for _ in range(n)]

diff = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def dijkstra(x, y):
    dist = [[INF for _ in range(m)] for _ in range(n)]
    dist[x][y] = 0
    pq = [(0, x, y)]
    while pq:
        cur_dist, x, y = hpop(pq)
        for dx, dy in diff:
            nx, ny = x + dx, y + dy
            if not ((0 <= nx < n) and (0 <= ny < m)):
                continue
            if (nxt_dist := abs(mt[nx][ny] - mt[x][y])) <= limit:
                if mt[nx][ny] <= mt[x][y]:
                    nxt_dist = 1
                nxt_dist = cur_dist + nxt_dist ** 2
                if dist[nx][ny] > nxt_dist:
                    dist[nx][ny] = nxt_dist
                    hpush(pq, (nxt_dist, nx, ny))
    return dist

forward = dijkstra(0, 0)
reachable = []
for x in range(n):
    for y in range(m):
        if forward[x][y] < dawn:
            hpush(reachable, (-mt[x][y], x, y))

while reachable:
    h, x, y = hpop(reachable)
    backward = dijkstra(x, y)
    if backward[0][0] + forward[x][y] <= dawn:
        print(-h)
        break

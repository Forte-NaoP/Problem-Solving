import sys
from collections import deque
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
heapify = heapq.heapify

input = sys.stdin.readline

diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    road = [list(input().strip()) for _ in range(n)]
    dist = [[10 ** 9 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if road[i][j] == 'A':
                sx, sy = i, j
                road[i][j] = '#'
            elif road[i][j] == 'B':
                tx, ty = i, j
                road[i][j] = '#'

    q = deque([(0, sx, sy)])
    dist[sx][sy] = 0
    cross = {}

    while (l := input()) != '\n':
        pi, d, a, b = l.strip().split()
        if d == '|':
            d = 1
            a, b = b, a
        else:
            d = 0
        cross[pi] = (d, int(a), int(b))

    while q:
        now, cx, cy = q.popleft()
        now += 1

        for dx, dy in diff:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < n) or not (0 <= ny < m):
                continue
            if road[nx][ny] == '.':
                continue

            wait = 0
            if road[nx][ny] != '#': # 교차로일 때
                d, a, b = cross[road[nx][ny]]
                cur = (now - 1) % (a + b)
                if dx == 0: # 가로 진입
                    if d == 0: # 교차로 가로 시작
                        if cur >= a:
                            wait = a + b - cur
                    else: # 교차로 세로 시작
                        if cur < a:
                            wait = a - cur
                else: # 세로 진입
                    if d == 0: # 교차로 가로 시작
                        if cur < a:
                            wait = a - cur
                    else:
                        if cur >= a:
                            wait = a + b - cur

            if dist[nx][ny] > now + wait:
                q.append((now + wait, nx, ny))
                dist[nx][ny] = now + wait
    
    print(dist[tx][ty] if dist[tx][ty] != 10 ** 9 else 'impossible')
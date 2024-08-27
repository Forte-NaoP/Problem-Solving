import sys
input = sys.stdin.readline

diff = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
row = col = range(100000)
n = int(input())
rx, ry = map(int, input().split())

dist = [[sys.maxsize for _ in range(5)] for _ in range(n + 1)]
for i, (dx, dy) in enumerate(diff):
    dist[0][i]= abs(dx) + abs(dy)

man = [(rx, ry)]
for _ in range(n):
    man.append(tuple(map(int, input().split())))


for i in range(1, n + 1):
    for j, (jdx, jdy) in enumerate(diff): # destination
        jx, jy = man[i][0] + jdx, man[i][1] + jdy
        if jx not in row or jy not in col:
            continue
        for k, (kdx, kdy) in enumerate(diff): # source
            kx, ky = man[i - 1][0] + kdx, man[i - 1][1] + kdy
            if kx not in row or ky not in col:
                continue
            dist[i][j] = min(dist[i][j], dist[i - 1][k] + abs(jx - kx) + abs(jy - ky))

print(min(dist[n]))
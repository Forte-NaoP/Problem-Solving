import sys
from collections import deque

INF = 1e9
diff = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n, m, t = map(int, input().split())
disk = [deque()]
total_cnt, total_num = 0, 0
for _ in range(n):
    disk.append(deque(map(int, input().split())))
    total_cnt += m
    total_num += sum(disk[-1])

for _ in range(t):
    x, d, k = map(int, input().split())

    for i in range(x, n + 1, x):
        if disk[i][0] != 0:
            for _ in range(k):
                if d == 0:
                    disk[i].appendleft(disk[i].pop())
                else:
                    disk[i].append(disk[i].popleft())
    rm = []
    for i in range(1, n + 1):
        for j in range(m):
            if disk[i][j] == INF:
                continue
            for dx, dy in diff:
                nx, ny = i + dx, (j + dy) % m
                if (1 <= nx <= n) and disk[nx][ny] == disk[i][j]:
                    rm.append((i, j))
                    rm.append((nx, ny))

    if rm:
        for rx, ry in rm:
            if disk[rx][ry] != INF:
                total_cnt -= 1
                total_num -= disk[rx][ry]
                disk[rx][ry] = INF
    else:
        if total_cnt == 0:
            break
        total_avg = total_num / total_cnt
        for i in range(1, n + 1):
            for j in range(m):
                if disk[i][j] == INF:
                    continue
                if disk[i][j] > total_avg:
                    disk[i][j] -= 1
                    total_num -= 1
                elif disk[i][j] < total_avg:
                    disk[i][j] += 1
                    total_num += 1

print(total_num)
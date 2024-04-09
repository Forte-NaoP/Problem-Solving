import sys
from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

ans = 999_999_999
alives = list(combinations(chicken, m))
for a in alives:
    score = 0
    for hx, hy in house:
        local_score = 999_999_999
        for cx, cy in a:
            local_score = min(local_score, abs(hx - cx) + abs(hy - cy))
        score += local_score
    ans = min(ans, score)
print(ans)
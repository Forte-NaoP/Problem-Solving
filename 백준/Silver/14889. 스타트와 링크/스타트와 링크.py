import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
user = [i for i in range(n)]
comb = list(combinations(user, n // 2))

ans = 1e9

for st in comb:
    li = [i for i in user if i not in st]
    st_ab = 0
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            st_ab += ab[st[i]][st[j]] + ab[st[j]][st[i]]

    li_ab = 0
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            li_ab += ab[li[i]][li[j]] + ab[li[j]][li[i]]
    
    ans = min(ans, abs(li_ab - st_ab))

print(ans)

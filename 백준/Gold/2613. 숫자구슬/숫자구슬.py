import sys

input = sys.stdin.readline

n, m = map(int, input().split())
bids = list(map(int, input().split()))

left, right = max(bids), sum(bids)
ans = right

while left <= right:
    mid = (left + right) // 2

    g_sum = 0
    g_cnt = 0
    group = []
    idx = 0
    while idx < n:
        if g_sum + bids[idx] > mid:
            group.append(g_cnt)
            g_sum = g_cnt = 0
        elif n - idx < m - len(group):
            group.append(g_cnt)
            g_sum = g_cnt = 0
        
        g_sum += bids[idx]
        g_cnt += 1
        idx += 1

    if g_cnt != 0:
        group.append(g_cnt)

    if len(group) <= m:
        if len(group) == m and ans > mid:
            ans = mid
            div = group
        right = mid - 1
    else:
        left = mid + 1

print(ans)
print(*div)
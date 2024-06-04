from collections import defaultdict

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))


def init(arr, size):
    prefix = [0, arr[0]]
    for i in range(1, size):
        prefix.append(prefix[-1] + arr[i])

    sum = {}
    for i in range(0, size):
        for j in range(i + 1, size + 1):
            if sum.get(prefix[j] - prefix[i]) is None: 
                sum[prefix[j] - prefix[i]] = 0
            sum[prefix[j] - prefix[i]] += 1

    return sum

a_sum = init(a, n)
b_sum = init(b, m)

ans = 0

for ak in a_sum.keys():
    if b_sum.get(t - ak):
        ans += a_sum[ak] * b_sum[t - ak]

print(ans)

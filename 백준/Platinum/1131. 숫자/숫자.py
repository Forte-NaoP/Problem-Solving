import sys

input = sys.stdin.readline

a, b, k = map(int, input().split())

pre_power = [[1] for i in range(10)]
for i in range(10):
    for j in range(6):
        pre_power[i].append(pre_power[i][-1] * i)

def pow_digit(x, p):
    ret = 0
    while x > 0:
        ret += pre_power[x % 10][p]
        x //= 10
    return ret

seq_min = {0: 0, 1: 1}
ans = 0
for i in range(a, b + 1):
    seq = [i]
    m = i
    while True:
        ret = pow_digit(seq[-1], k)
        if ret in seq_min:
            m = seq_min[ret]
            for j in range(len(seq) - 1, -1, -1):
                m = min(m, seq[j])
                seq_min[seq[j]] = m
            break
        if ret in seq:
            idx = seq.index(ret)
            m = seq[idx]
            for j in range(idx, len(seq)):
                m = min(m, seq[j])
            for j in range(idx, len(seq)):
                seq_min[seq[j]] = m
            for j in range(idx - 1, -1, -1):
                m = min(m, seq[j])
                seq_min[seq[j]] = m
            break
        seq.append(ret)
        m = min(m, ret)
    ans += m

print(ans)
import sys

input = sys.stdin.readline

D, P, Q = map(int, input().split())
P, Q = max(P, Q), min(P, Q)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

PQ = P * Q // gcd(P, Q)
ans = 1 << 31
for aP in range(0, min(D, PQ) + P, P):
    R = max(D - aP, 0)
    b = R // Q
    if R % Q != 0:
        b += 1
    ans = min(ans, aP + b * Q)

print(ans)
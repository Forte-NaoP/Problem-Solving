import sys
input = sys.stdin.readline

n, k = map(int, input().split())
fact = [1, 1]
for i in range(2, 20):
    fact.append(fact[-1] * i)

print(fact[n] // (fact[k] * fact[n - k]))
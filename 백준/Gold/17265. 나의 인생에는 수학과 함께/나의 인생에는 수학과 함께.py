import sys
import operator

n = int(input())
op = {'+': operator.add, '-': operator.sub, '*': operator.mul}
route = [input().split() for _ in range(n)]
m = [[1e9 for _ in range(n)] for _ in range(n)]
M = [[-1e9 for _ in range(n)] for _ in range(n)]
m[0][0] = M[0][0] = int(route[0][0])

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        if i % 2 == j % 2:
            if i > 0:
                m[i][j] = min(m[i][j], op[route[i - 1][j]](m[i - 1][j], int(route[i][j])))
                M[i][j] = max(M[i][j], op[route[i - 1][j]](M[i - 1][j], int(route[i][j])))
            if j > 0:
                m[i][j] = min(m[i][j], op[route[i][j - 1]](m[i][j - 1], int(route[i][j])))
                M[i][j] = max(M[i][j], op[route[i][j - 1]](M[i][j - 1], int(route[i][j])))
        else:
            if i > 0:
                m[i][j] = min(m[i][j], m[i - 1][j])
                M[i][j] = max(M[i][j], M[i - 1][j])
            if j > 0:
                m[i][j] = min(m[i][j], m[i][j - 1])
                M[i][j] = max(M[i][j], M[i][j - 1])

print(M[-1][-1], m[-1][-1])

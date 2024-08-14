import sys

input = sys.stdin.readline
n, m = map(int, input().split())

def backtrack(seq, depth, after):
    if depth == m:
        print(' '.join(map(str, seq)))
        return
    for num in range(after, n + 1):
        seq.append(num)
        backtrack(seq, depth + 1, num)
        seq.pop()

backtrack([], 0, 1)
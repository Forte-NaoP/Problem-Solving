import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted(set(map(int, input().split())))

def backtrack(seq, depth, after):
    if depth == m:
        print(' '.join(map(str, seq)))
        return
    for idx in range(after, len(nums)):
        seq.append(nums[idx])
        backtrack(seq, depth + 1, idx)
        seq.pop()

backtrack([], 0, 0)
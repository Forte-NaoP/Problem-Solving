import sys
from operator import add, sub, mul, floordiv

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
op_num = list(map(int, input().split()))
op = [add, sub, mul, lambda x, y : int(x / y)]

M, m = -1e9, 1e9

def do_op(val, idx):
    global M, m, n
    if idx == n:
        m = min(val, m)
        M = max(val, M)
        return

    for i in range(4):
        if op_num[i] != 0:
            op_num[i] -= 1
            do_op(op[i](val, nums[idx]), idx + 1)
            op_num[i] += 1

do_op(nums[0], 1)
print(M)
print(m)
import sys
import operator as op
from collections import deque
from copy import deepcopy
import math

n = int(input())
line = deque(input().rstrip())
act = {'+': op.add, '-': op.sub, '*': op.mul}

max_ans = -math.inf

def calc(eq: deque, seq: deque):
    global max_ans

    if len(eq) < 3:
        if eq:
            seq.append(int(eq.popleft()))
        
        a = seq.popleft()
        while seq:
            o, b = seq.popleft(), int(seq.popleft())
            a = act[o](a, b)
        max_ans = max(max_ans, a)
        return

    eq_a = deepcopy(eq)
    seq_a = deepcopy(seq)

    a, o = int(eq_a.popleft()), eq_a.popleft()
    seq_a.extend([a, o])
    calc(eq_a, seq_a)

    eq_b = deepcopy(eq)
    seq_b = deepcopy(seq)
    a, o, b = int(eq_b.popleft()), eq_b.popleft(), int(eq_b.popleft())
    a = act[o](a, b)
    if eq_b:
        seq_b.extend([a, eq_b.popleft()])
    else:
        seq_b.append(a)

    calc(eq_b, seq_b)

calc(line, deque())
print(max_ans)

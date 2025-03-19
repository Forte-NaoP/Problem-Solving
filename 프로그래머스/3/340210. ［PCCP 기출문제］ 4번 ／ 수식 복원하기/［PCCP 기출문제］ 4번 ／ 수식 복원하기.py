def to_decimal(val, base):
    ret = 0
    d = len(val)
    for idx, c in enumerate(val):
        if int(c) >= base:
            return -1
        ret += int(c) * (base ** (d - idx - 1))
    return ret

def to_base(val, base):
    ret = ''
    a = base ** 2
    while a > val:
        a //= base
    
    while a > 0:
        ret += str(val // a)
        val %= a
        a //= base
    if ret == '':
        ret = '0'
    return ret
    
def solution(expressions):
    possible = [True for _ in range(10)]
    from operator import add, sub
    ops = {'+': add, '-': sub}
    
    equations = []
    for exp in expressions:
        a, op, b, e, c = exp.split()
        if c == 'X':
            equations.append((a, op, b, e))
        for base in range(2, 10):
            da = to_decimal(a, base)
            db = to_decimal(b, base)
            if da == -1 or db == -1:
                possible[base] = False
            if c != 'X':
                dc = to_decimal(c, base)
                if dc == -1 or ops[op](da, db) != dc:
                    possible[base] = False
    
    answer = []
    for exp in equations:
        a, op, b, e = exp
        vals = dict()
        for base in range(2, 10):
            if possible[base]:
                da = to_decimal(a, base)
                db = to_decimal(b, base)
                if da == -1 or db == -1:
                    continue
                vals[to_base(ops[op](da, db), base)] = base
        print(vals)
        if len(vals) > 1:
            answer.append(f'{a} {op} {b} {e} ?')
        else:
            for c, base in vals.items():
                answer.append(f'{a} {op} {b} {e} {c}')
                
    return answer
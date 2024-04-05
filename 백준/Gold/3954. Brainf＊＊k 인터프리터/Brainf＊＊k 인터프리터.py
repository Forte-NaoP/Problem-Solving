import sys

def dsc():
    global sp
    mem[sp] = (mem[sp] - 1) % 256

def inc():
    global sp
    mem[sp] = (mem[sp] + 1) % 256

def left():
    global sp, size
    sp = (sp - 1) % size

def right():
    global sp, size
    sp = (sp + 1) % size

def jz():
    global pc, sp
    if mem[sp] == 0:
        pc = jmp_map[pc]

def jnz():
    global pc, sp
    if mem[sp] != 0:
        pc = jmp_map[pc]

def write():
    pass

def read():
    global fp, sp
    mem[sp] = ord(stdin[fp]) if fp != feof else 255
    fp = min(fp + 1, feof)

def nop():
    pass

pc, peof, sp, size, fp, feof = 0, 0, 0, 0, 0, 0
mem = [0 for _ in range(100_000)]
jmp_stack = []
jmp_map = {}

stdin = ''

op_chr = ['-', '+', '<', '>', '[', ']', '.', ',']
op_set = [nop for _ in range(100)]
op_set[ord('-')] = dsc
op_set[ord('+')] = inc
op_set[ord('<')] = left
op_set[ord('>')] = right
op_set[ord('[')] = jz
op_set[ord(']')] = jnz
op_set[ord('.')] = write
op_set[ord(',')] = read

limit = 50_000_000

tc = int(input())
for _ in range(tc):
    size, peof, feof = map(int, input().split())
    code = input().strip()
    stdin = input().strip()

    jmp_map.clear()
    for i in range(size):
        mem[i] = 0
    pc, sp, fp = 0, 0, 0

    for i in range(peof):
        if code[i] == '[':
            jmp_stack.append(i)
        elif code[i] == ']':
            jmp_l = jmp_stack.pop()
            jmp_map[jmp_l] = i
            jmp_map[i] = jmp_l

    counter = 0
    max_pc = 0
    result = 'Terminates'
    while pc < peof:
        counter += 1
        op_set[ord(code[pc])]()
        pc += 1
        
        if counter >= limit:
            max_pc = max(max_pc, pc)
        if counter >= limit * 2:
            result = f'Loops {jmp_map[max_pc]} {max_pc}'
            break
    
    print(result)
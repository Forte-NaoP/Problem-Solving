import copy

UNIT = [
    '  *  ',
    ' * * ',
    '*****'
]
SPACE = ' '
BLANK = '   '

def make_block(depth):
    size = 2
    buffer = [copy.deepcopy(UNIT), []]
    b_idx = 0
    while size <= depth:
        blank_size = size // 2
        upper = []
        for buff in buffer[b_idx]:
            upper.append(BLANK * blank_size + buff + BLANK * blank_size)
        lower = []
        for buff in buffer[b_idx]:
            lower.append(buff + ' ' + buff)

        buffer[b_idx ^ 1] = upper + lower
        b_idx ^= 1
        size *= 2
        
    return buffer[b_idx]

n = int(input())
buffer = make_block(n // 3)
for buf in buffer:
    print(buf)
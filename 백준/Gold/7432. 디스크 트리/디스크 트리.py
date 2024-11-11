import sys

input = lambda : sys.stdin.readline().strip()

n = int(input())
dirs = [list(input().split('\\')) for _ in range(n)]
dirs.sort()
stack = []
res = ''

for dir in dirs:
    for depth, name in enumerate(dir):
        if depth < len(stack) and name == stack[depth]:
            continue
        st_len = len(stack)
        for _ in range(max(0, st_len - depth)):
            stack.pop()
        res += f"{' ' * depth}{name}\n"
        stack.append(name)
print(res)
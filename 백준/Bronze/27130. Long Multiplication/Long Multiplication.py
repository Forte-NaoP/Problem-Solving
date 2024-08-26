import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
c = b

print(f'{a}\n{b}')
while c != 0:
    print(a * (c % 10))
    c //= 10

print(a * b)
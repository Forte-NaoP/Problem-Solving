n = int(input())
a, b, c = map(int, input().split())
small = [a, b, c]
big = [a, b, c]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    small = [min(small[:2]) + a, min(small) + b, min(small[1:]) + c]
    big = [max(big[:2]) + a, max(big) + b, max(big[1:]) + c]
    
print(max(big), min(small))
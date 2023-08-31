import sys

input = sys.stdin.readline

x1, y1, x2, y2 = list(map(int, input().strip().split(' ')))
x3, y3, x4, y4 = list(map(int, input().strip().split(' ')))

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2 + x2*y3 + x3*y1 - (x2*y1 + x3*y2 + x1*y3)

abc = ccw(x1, y1, x2, y2, x3, y3)
abd = ccw(x1, y1, x2, y2, x4, y4)
cda = ccw(x3, y3, x4, y4, x1, y1)
cdb = ccw(x3, y3, x4, y4, x2, y2)

if abc * abd == 0 and cda * cdb == 0:
    if (min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and
        min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2)):
        print(1)
    else:
        print(0)
else:
    if abc * abd <= 0 and cda * cdb <= 0:
        print(1)
    else:
        print(0)


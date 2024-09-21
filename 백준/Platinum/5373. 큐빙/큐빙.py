import sys

input = sys.stdin.readline

class Square:
    def __init__(self, c):
        self.c = c
        self.s = [c for _ in range(9)]
        self.adj = []

    def clear(self):
        for i in range(9):
            self.s[i] = self.c

    def connect(self, *args):
        for adj in args:
            self.adj.append(adj)

    def left(self):
        self.transpose()
        for j in range(3):
            self.s[j], self.s[6 + j] = self.s[6 + j], self.s[j]

        tmp = [self.adj[0][0].s[i] for i in range(*self.adj[0][1])]
        for i in range(3):
            for x, y in zip(range(*self.adj[i][1]), range(*self.adj[(i + 1) % 4][1])):
                self.adj[i][0].s[x] = self.adj[(i + 1) % 4][0].s[y]

        for x, y in zip(range(*self.adj[3][1]), range(3)):
            self.adj[3][0].s[x] = tmp[y]


    def right(self):
        self.transpose()
        for i in range(3):
            self.s[i * 3], self.s[i * 3 + 2] = self.s[i * 3 + 2], self.s[i * 3]

        tmp = [self.adj[-1][0].s[i] for i in range(*self.adj[-1][1])]
        for i in range(3, 0, -1):
            for x, y in zip(range(*self.adj[i][1]), range(*self.adj[i - 1][1])):
                self.adj[i][0].s[x] = self.adj[i - 1][0].s[y]

        for x, y in zip(range(*self.adj[0][1]), range(3)):
            self.adj[0][0].s[x] = tmp[y]

    def transpose(self):
        for i in range(3):
            for j in range(i + 1, 3):
                self.s[i * 3 + j], self.s[j * 3 + i] = self.s[j * 3 + i], self.s[i * 3 + j]

U = Square('w')
D = Square('y')
F = Square('r')
B = Square('o')
L = Square('g')
R = Square('b')

U.connect((F, (0, 3, 1)), (L, (0, 3, 1)), (B, (0, 3, 1)), (R, (0, 3, 1)))
D.connect((F, (6, 9, 1)), (R, (6, 9, 1)), (B, (6, 9, 1)), (L, (6, 9, 1)))
L.connect((U, (0, 9, 3)), (F, (0, 9, 3)), (D, (0, 9, 3)), (B, (8, -1, -3)))
R.connect((U, (2, 9, 3)), (B, (6, -1, -3)), (D, (2, 9, 3)), (F, (2, 9, 3)))
F.connect((U, (6, 9, 1)), (R, (0, 9, 3)), (D, (2, -1, -1)), (L, (8, -1, -3)))
B.connect((U, (2, -1, -1)), (L, (0, 9, 3)), (D, (6, 9, 1)), (R, (8, -1, -3)))

cube = {'U': U, 'D': D, 'F': F, 'B': B, 'L': L, 'R': R}

def parr(arr):
    for i in range(3):
        for j in range(3):
            print(arr[i * 3 + j], end='')
        print()

for _ in range(int(input())):
    for k in cube.keys():
        cube[k].clear()
    input()
    cmd = input().split()
    for c, d in cmd:
        if d == '-':
            cube[c].left()
        else:
            cube[c].right()
    parr(U.s)

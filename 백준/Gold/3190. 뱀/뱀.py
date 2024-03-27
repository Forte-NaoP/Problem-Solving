import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 2

board[0][0] = 1
snake = deque([(0, 0)])
head = 0
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
sec = 0
turn = deque()
m = int(input())

for _ in range(m):
    x, c = input().split()
    x = int(x)
    turn.append((x, c))

def move():
    global head, turn
    hx, hy = snake[0]
    hx += d[head][0]
    hy += d[head][1]

    if turn and turn[0][0] == sec:
        if turn[0][1] == 'D':
            head = (head + 1) % 4
        else:
            head = (head + 3) % 4
        turn.popleft()

    if (0 <= hx < n) and (0 <= hy < n):
        if board[hx][hy] == 1:
            return False
        
        if board[hx][hy] != 2:
            tx, ty = snake.pop()
            board[tx][ty] = 0
        
        board[hx][hy] = 1
        snake.appendleft((hx, hy))

    else:
        return False
    
    return True

while True:
    sec += 1
    alive = move()
    if not alive:
        break
print(sec)
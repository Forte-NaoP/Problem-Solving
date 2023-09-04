def solution(board):
    for i in range(len(board)):
        for j in range(len(board)):
            board[i][j] = [board[i][j], 0, 0, 999999999]

    board[-1][-1][3] = 0

    from collections import deque
    n = len(board)
    queue = deque()
    queue.append((n-1, n-1, n-1, n-1, 0))
    while len(queue) != 0:
        bx, by, x, y, c = queue.popleft()

        if x > 0 and board[x - 1][y][0] == 0:
            if by == y:
                if board[x - 1][y][3] >= c + 100:
                    board[x - 1][y][1:] = [x, y, c + 100]
                    queue.append((x, y, x - 1, y, c + 100))
            else:
                if board[x - 1][y][3] >= c + 600:
                    board[x - 1][y][1:] = [x, y, c + 600]
                    queue.append((x, y, x - 1, y, c + 600))
        if x < len(board) - 1 and board[x + 1][y][0] == 0:
            if by == y:
                if board[x + 1][y][3] >= c + 100:
                    board[x + 1][y][1:] = [x, y, c + 100]
                    queue.append((x, y, x + 1, y, c + 100))
            else:
                if board[x + 1][y][3] >= c + 600:
                    board[x + 1][y][1:] = [x, y, c + 600]
                    queue.append((x, y, x + 1, y, c + 600))
        if y > 0 and board[x][y - 1][0] == 0:
            if bx == x:
                if board[x][y - 1][3] >= c + 100:
                    board[x][y - 1][1:] = [x, y, c + 100]
                    queue.append((x, y, x, y - 1, c + 100))
            else:
                if board[x][y - 1][3] >= c + 600:
                    board[x][y - 1][1:] = [x, y, c + 600]
                    queue.append((x, y, x, y - 1, c + 600))
        if y < len(board) - 1 and board[x][y + 1][0] == 0:
            if bx == x:
                if board[x][y + 1][3] >= c + 100:
                    board[x][y + 1][1:] = [x, y, c + 100]
                    queue.append((x, y, x, y + 1, c + 100))
            else:
                if board[x][y + 1][3] >= c + 600:
                    board[x][y + 1][1:] = [x, y, c + 600]
                    queue.append((x, y, x, y + 1, c + 600))
    answer = board[0][0][-1]
    return answer
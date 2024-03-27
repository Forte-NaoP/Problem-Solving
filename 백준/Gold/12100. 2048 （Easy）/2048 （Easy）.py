import sys
import copy

input = sys.stdin.readline

n = int(input())

tile = [list(map(int, input().split())) for _ in range(n)]

ans = max(map(max, tile))

def move(board, d):
    if d == 0:
        for i in range(n):
            j = 0
            while j < n and board[j][i] == 0:
                j += 1

            while j < n:
                k = j + 1
                while k < n:
                    if board[k][i] != 0:
                        if board[j][i] == board[k][i]:
                            board[j][i] += board[k][i]
                            board[k][i] = 0
                            j = k + 1
                        else:
                            j = k
                        break
                    k += 1
                if k == n:
                    break
            
            a = []
            for k in range(n):
                if board[k][i] != 0:
                    a.append(board[k][i])

            for k in range(n):
                if k >= len(a):
                    board[k][i] = 0
                else:
                    board[k][i] = a[k]
                            
    elif d == 1:
        for i in range(n):
            j = 0
            while j < n and board[i][j] == 0:
                j += 1

            while j < n:
                k = j + 1
                while k < n:
                    if board[i][k] != 0:
                        if board[i][j] == board[i][k]:
                            board[i][j] += board[i][k]
                            board[i][k] = 0
                            j = k + 1
                        else:
                            j = k
                        break
                    k += 1
                if k == n:
                    break
            
            a = []
            for k in range(n):
                if board[i][k] != 0:
                    a.append(board[i][k])

            for k in range(n):
                if k >= len(a):
                    board[i][k] = 0
                else:
                    board[i][k] = a[k]
    elif d == 2:
        for i in range(n):
            j = n - 1
            while j >= 0 and board[j][i] == 0:
                j -= 1

            while j >= 0:
                k = j - 1
                while k >= 0:
                    if board[k][i] != 0:
                        if board[j][i] == board[k][i]:
                            board[j][i] += board[k][i]
                            board[k][i] = 0
                            j = k - 1
                        else:
                            j = k
                        break
                    k -= 1
                if k == -1:
                    break
            
            a = []
            for k in range(n - 1, -1, -1):
                if board[k][i] != 0:
                    a.append(board[k][i])

            for k in range(n):
                if k >= len(a):
                    board[n - 1 - k][i] = 0
                else:
                    board[n - 1 - k][i] = a[k]
    else:
        for i in range(n):
            j = n - 1
            while j >= 0 and board[i][j] == 0:
                j -= 1

            while j >= 0:
                k = j - 1
                while k >= 0:
                    if board[i][k] != 0:
                        if board[i][j] == board[i][k]:
                            board[i][j] += board[i][k]
                            board[i][k] = 0
                            j = k - 1
                        else:
                            j = k
                        break
                    k -= 1
                if k == -1:
                    break
            
            a = []
            for k in range(n - 1, -1, -1):
                if board[i][k] != 0:
                    a.append(board[i][k])

            for k in range(n):
                if k >= len(a):
                    board[i][n - 1 - k] = 0
                else:
                    board[i][n - 1 - k] = a[k]

    return board

def dfs(board, cnt):
    global ans
    if cnt == 5:
        return

    for i in range(4):
        after = move(copy.deepcopy(board), i)
        ans = max(ans, max(map(max, after)))
        dfs(after, cnt + 1)

dfs(tile, 0)
print(ans)

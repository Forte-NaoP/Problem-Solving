def solution(maze):
    n = len(maze)
    m = len(maze[0])
    
    rsx, rsy, rex, rey = -1, -1, -1, -1
    bsx, bsy, bex, bey = -1, -1, -1, -1
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                rsx, rsy = i, j
            if maze[i][j] == 2:
                bsx, bsy = i, j
            if maze[i][j] == 3:
                rex, rey = i, j
            if maze[i][j] == 4:
                bex, bey = i, j
    
    row = range(n)
    col = range(m)
    diff = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    
    r_visit = [[False for _ in range(m)] for _ in range(n)]
    b_visit = [[False for _ in range(m)] for _ in range(n)]
    
    def search(rx, ry, bx, by, cnt):
        if rx == rex and ry == rey and bx == bex and by == bey:
            return cnt
        
        r_move = []
        if rx == rex and ry == rey:
            r_move.append((rx, ry))
        else:
            for rdx, rdy in diff:
                rnx, rny = rx + rdx, ry + rdy
                if rnx not in row or rny not in col:
                    continue
                if r_visit[rnx][rny] or maze[rnx][rny] == 5:
                    continue
                r_move.append((rnx, rny))
            
        b_move = []
        if bx == bex and by == bey:
            b_move.append((bx, by))
        else:
            for bdx, bdy in diff:
                bnx, bny = bx + bdx, by + bdy
                if bnx not in row or bny not in col:
                    continue
                if b_visit[bnx][bny] or maze[bnx][bny] == 5:
                    continue
                b_move.append((bnx, bny))
        
        ans = 10 ** 9
        for i in range(len(r_move)):
            for j in range(len(b_move)):
                if r_move[i] == b_move[j]:
                    continue
                if r_move[i] == (bx, by) and b_move[j] == (rx, ry):
                    continue
                r_visit[r_move[i][0]][r_move[i][1]] = True
                b_visit[b_move[j][0]][b_move[j][1]] = True
                ans = min(ans, search(*r_move[i], *b_move[j], cnt + 1))
                r_visit[r_move[i][0]][r_move[i][1]] = False
                b_visit[b_move[j][0]][b_move[j][1]] = False
                
        return ans
    r_visit[rsx][rsy] = True
    b_visit[bsx][bsy] = True
    answer = search(rsx, rsy, bsx, bsy, 0)
    return answer if answer != 10 ** 9 else 0
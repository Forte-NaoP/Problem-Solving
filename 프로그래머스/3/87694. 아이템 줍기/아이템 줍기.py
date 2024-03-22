from collections import deque

def is_border(border_x, border_y, x, y):
    for bx, s, e in border_x:
        if x == bx and s <= y <= e:
            return True
        
    for by, s, e in border_y:
        if y == by and s <= x <= e:
            return True
        
    return False

def is_inside(rectangle, x, y):
    ret = False
    
    for rect in rectangle:
        ret |= (rect[0] < x < rect[2]) and (rect[1] < y < rect[3])
    
    return ret
        
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    border_x = []
    border_y = []

    for rect in rectangle:
        border_x.append((rect[0], rect[1], rect[3]))
        border_x.append((rect[2], rect[1], rect[3]))
        border_y.append((rect[1], rect[0], rect[2]))
        border_y.append((rect[3], rect[0], rect[2]))
    
    d = [(0.5, 0), (-0.5, 0), (0, 0.5), (0, -0.5)]
    visit = [[0 for _ in range(52)] for _ in range(52)]
    q = deque()
    
    q.append((characterX, characterY, 0))
    visit[characterX][characterY] = 1
    
    while q:
        x, y, cost = q.popleft()
        if x == itemX and y == itemY:
            answer = cost
            break
        
        for dx, dy in d:
            nhx, nhy = x + dx, y + dy
            nx, ny = int(x + dx * 2), int(y + dy * 2)
            if is_border(border_x, border_y, nhx, nhy) and not is_inside(rectangle, nx, ny) and not is_inside(rectangle, nhx, nhy):
                if not visit[nx][ny]:
                    q.append((nx, ny, cost + 1))
                    visit[nx][ny] = 1
                
    return answer
import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
rx, ry, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
clean = 0

def work():
    global n, m, rx, ry, d, clean
    if room[rx][ry] == 0:
        room[rx][ry] = -1
        clean += 1
    
    td = d
    for _ in range(4):
        td = (td + 3) % 4
        nx, ny =  rx + dx[td], ry + dy[td]
        if room[nx][ny] == 0:
            rx, ry, d = nx, ny, td
            return True
    
    nx, ny =  rx - dx[d], ry - dy[d]
    if (0 <= nx < n) and (0 <= ny < m) and room[nx][ny] != 1:
        rx, ry = nx, ny 
        return True
    
    return False

while work():
    pass

print(clean)
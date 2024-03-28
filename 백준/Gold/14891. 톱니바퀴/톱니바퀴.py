import sys
input = sys.stdin.readline

gear = [list(map(int, list(input().strip()))) for _ in range(4)]

def roll(i, d):
    if d == 1:
        gear[i] = gear[i][-1:] + gear[i][:-1]
    elif d == -1:
        gear[i] = gear[i][1:] + gear[i][:1]
    else:
        return

k = int(input())
for _ in range(k):
    i, d = map(int, input().split())
    i -= 1

    roll_cmd = [0, 0, 0, 0]
    roll_cmd[i] = d

    r = d
    for j in range(i, 3):
        if gear[j][2] == gear[j + 1][6]:
            break
        if r == 1:
            roll_cmd[j + 1] = -1
            r = -1
        else:
            roll_cmd[j + 1] = 1
            r = 1
    r = d
    for j in range(i, 0, -1):
        if gear[j][6] == gear[j - 1][2]:
            break
        if r == 1:
            roll_cmd[j - 1] = -1
            r = -1
        else:    
            roll_cmd[j - 1] = 1
            r = 1

    for j, r in enumerate(roll_cmd):
        roll(j, r)

ans = 0
score = 1
for g in gear:
    if g[0]:
        ans += score
    score <<= 1

print(ans)

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, k = map(int, input().split())
dp = [[[-1 for _ in range(m + 1)] for _ in range(n + 1)] for _ in range(n + m + 1)]

# dp[i][x][y] : x개의 'a'와 y개의 'z'를 가지고 i번째 문자를 채우는 경우의 수
# dp[i][x][y] = dp[i + 1][x - 1][y] (i번째 문자를 a로 할 경우) + dp[i + 1][x][y - 1] (i번째 문자를 z로 할 경우)

def make_str(i, a, z):
    if dp[i][a][z] != -1:
        return dp[i][a][z]
    
    if a == 0 and z == 0:
        dp[i][a][z] = 1
        return 1
    
    tmp = 0
    if a > 0:
        tmp += make_str(i + 1, a - 1, z)
    if z > 0:
        tmp += make_str(i + 1, a, z - 1)

    dp[i][a][z] = tmp
    return tmp

make_str(0, n, m)
if dp[1][n - 1][m] + dp[1][n][m - 1] < k:
    print(-1)
else:
    word = ['' for _ in range(n + m)]
    idx = 1
    a, z = n, m

    while idx <= n + m:
        if k > dp[idx][a - 1][z]:
            k -= dp[idx][a - 1][z]
            word[idx - 1] = 'z'
            z -= 1
        else:
            word[idx - 1] = 'a'
            a -= 1
        idx += 1
    print(''.join(word))
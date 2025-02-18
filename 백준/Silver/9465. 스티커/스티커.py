T = int(input())
'''
def score_sticker(n, m):
    if n == 0 and m == 0:
        dp[n][m] = sticker[0][0]
        return dp[n][m]
    elif n == 1 and m == 0:
        dp[n][m] = sticker[1][0]
        return dp[n][m]
    elif n == 0 and m == 1:
        dp[n][m] = sticker[1][0] + sticker[0][1]
        return dp[n][m]
    elif n == 1 and m == 1:
        dp[n][m] = sticker[0][0] + sticker[1][1]
        return dp[n][m]
    if dp[n][m]:
        return dp[n][m]
    dp[n][m] = max(score_sticker((n+1)%2, m-1) + sticker[n][m], 
                   score_sticker((n+1)%2, m-2) + sticker[n][m])
    return dp[n][m]
'''
for _ in range(T):
    N = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * N for _ in range(2)]

    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    
    if N > 1:
        dp[0][1] = sticker[0][1] + dp[1][0]
        dp[1][1] = sticker[1][1] + dp[0][0]

    for m in range(2, N):
        dp[0][m] = max(dp[1][m-1], dp[1][m-2]) + sticker[0][m]
        dp[1][m] = max(dp[0][m-1], dp[0][m-2]) + sticker[1][m]

    answer = max(dp[0][N-1], dp[1][N-1])
    print(answer)
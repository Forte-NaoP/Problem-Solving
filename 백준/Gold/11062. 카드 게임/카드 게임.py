import sys
input = sys.stdin.readline

dp = [[-1 for _ in range(1000)] for _ in range(1000)]

def recur(st, ed, deck, turn):  
    if st > ed:
        return 0
    if dp[st][ed] != -1:
        return dp[st][ed]
    
    if turn == 0:
        dp[st][ed] = max(
            deck[st] + recur(st + 1, ed, deck, turn ^ 1), 
            deck[ed] + recur(st, ed - 1, deck, turn ^ 1)
        )
    else:
        dp[st][ed] = min(
            recur(st + 1, ed, deck, turn ^ 1), 
            recur(st, ed - 1, deck, turn ^ 1)
        )
    return dp[st][ed]
    
t = int(input())
for _ in range(t):
    n = int(input())
    deck = list(map(int, input().split()))
    
    for i in range(n):
        for j in range(n):
            dp[i][j] = -1
    recur(0, n - 1, deck, 0)
    print(dp[0][n - 1])
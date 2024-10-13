import sys

input = sys.stdin.readline

s = input().strip()
n = int(input())
words = [input().strip() for _ in range(n)]
words.sort(key=lambda x: len(x), reverse=True)
dp = [-1 for _ in range(len(s) + 1)]

def recur(st):
    if st == len(s):
        return 1
    if dp[st] != -1:
        return dp[st]
    dp[st] = 0
    for word in words:
        if st + len(word) <= len(s) and s[st:st+len(word)] == word:
            dp[st] |= recur(st + len(word))
    return dp[st]

print(recur(0))

import sys

input = sys.stdin.readline

def get_pi(s):
    begin, matched = 1, 0
    pi = [0 for _ in range(len(s))]

    while begin + matched < len(s):
        if s[begin + matched] == s[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi

s = input().strip()
ans = 0
for i in range(len(s)):
    ans = max(ans, max(get_pi(s[i:])))
print(ans)


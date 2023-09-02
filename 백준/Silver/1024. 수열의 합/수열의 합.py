import sys

input = sys.stdin.readline


def solution(n, L):
    answer = 0

    diff = L * (L-1) // 2
    while diff <= n:
        if (n-diff) % L == 0:
            return [i+(n-diff)//L for i in range(L)]
        else:
            L += 1
            diff = L * (L - 1) // 2
    return None


if __name__ == "__main__":
    n, L = map(int, input().split())
    if (ans := solution(n, L)) is None or len(ans) > 100:
        print(-1)
    else:
        print(' '.join(map(str, ans)))


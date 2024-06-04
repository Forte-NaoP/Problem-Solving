t = int(input())
for _ in range(t):
    n = int(input())
    want = [0] + list(map(int, input().split()))
    st = []
    visit = [False for _ in range(n + 1)]
    cycle = 0

    for i in range(1, n + 1):
        if visit[i]:
            continue
        st.append(i)
        visit[i] = True

        while st:
            now = st[-1]
            if not visit[want[now]]:
                st.append(want[now])
                visit[want[now]] = True
            else:
                cut = -1
                if want[now] in st:
                    cut = st.index(want[now])
                    cycle += len(st) - cut
                st = []
    print(n - cycle)
t = int(input())
for _ in range(t):
    n = int(input())
    want = [0] + list(map(int, input().split()))
    st = []
    visit = [False for _ in range(n + 1)]
    cycle = [0 for _ in range(n + 1)]

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
                if cycle[want[now]] != 0:
                    while st:
                        cycle[st.pop()] = -1
                else:
                    while st and st[-1] != want[now]:
                        cycle[st.pop()] = 1
                    if st:
                        cycle[st.pop()] = 1
                    while st:
                        cycle[st.pop()] = -1
                        
    print(cycle.count(-1))
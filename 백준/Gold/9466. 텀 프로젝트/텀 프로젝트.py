t = int(input())
for _ in range(t):
    n = int(input())
    want = [0] + list(map(int, input().split()))
    st = []
    not_visit = set([i for i in range(1, n + 1)])
    not_cycle = set()
    cycle = set()

    while not_visit:
        cur = not_visit.pop()
        st.append(cur)

        while st:
            now = st[-1]
            if want[now] in not_visit:
                st.append(want[now])
                not_visit.remove(want[now])
            else:
                if want[now] in cycle or want[now] in not_cycle:
                    not_cycle.update(st)
                    st.clear()
                else:
                    while st and st[-1] != want[now]:
                        cycle.add(st.pop())
                    if st:
                        cycle.add(st.pop())
                    not_cycle.update(st)
                    st.clear()
    print(len(not_cycle))
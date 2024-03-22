from collections import defaultdict

def solution(tickets):
    port = defaultdict(list)
    
    for src, dst in tickets:
        port[src].append(dst)
    
    for k in port.keys():
        port[k].sort(reverse=True)

    route = []
    st = ["ICN"]
    cur = "ICN"
    while st:
        cur = st[-1]
        if port[cur]:
            nxt = port[cur].pop()
            st.append(nxt)
        else:
            route.append(st.pop())
        
    return route[::-1]
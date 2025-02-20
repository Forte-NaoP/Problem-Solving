from collections import defaultdict


def iterative_dfs(start):
    stack = [(start, 0)]
    visited[start] = True

    while stack:
        node, depth = stack.pop()
        depth_table[node] = depth

        for child in graph[node]:
            if not visited[child]:
                parent_table[child][0] = node
                visited[child] = True
                stack.append((child, depth + 1))


def prepare_lca(N):
    for i in range(1, 20):
        for node in range(1, N + 1):
            if parent_table[node][i - 1] != -1:
                parent_table[node][i] = parent_table[parent_table[node][i - 1]][i - 1]


def lca(node1, node2):
    if depth_table[node1] < depth_table[node2]:
        node1, node2 = node2, node1

    diff = depth_table[node1] - depth_table[node2]
    for i in range(20):
        if (diff >> i) & 1:
            node1 = parent_table[node1][i]

    if node1 == node2:
        return node1

    for i in range(19, -1, -1):
        if parent_table[node1][i] != parent_table[node2][i]:
            node1 = parent_table[node1][i]
            node2 = parent_table[node2][i]

    return parent_table[node1][0]


N = int(input())
graph = defaultdict(list)

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
parent_table = [[-1] * 20 for _ in range(N + 1)]
depth_table = [0] * (N + 1)

iterative_dfs(1)
prepare_lca(N)

M = int(input())
for _ in range(M):
    node1, node2 = map(int, input().split())
    print(lca(node1, node2))
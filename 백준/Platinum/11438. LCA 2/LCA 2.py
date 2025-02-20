import sys
from collections import defaultdict, deque

def dfs_stack(root):
    stack = [root]
    visited[root] = True
    depth_table[root] = 0
    while stack:
        node = stack.pop()
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                depth_table[child] = depth_table[node] + 1
                parent_table[child][0] = node
                stack.append(child)


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


input = sys.stdin.read
data = input().split()

N = int(data[0])
graph = defaultdict(list)
index = 1

for _ in range(N - 1):
    u, v = int(data[index]), int(data[index + 1])
    graph[u].append(v)
    graph[v].append(u)
    index += 2

visited = [False] * (N + 1)
parent_table = [[-1] * 20 for _ in range(N + 1)]
depth_table = [0] * (N + 1)

dfs_stack(1)
prepare_lca(N)

M = int(data[index])
index += 1
output = []
for _ in range(M):
    node1, node2 = int(data[index]), int(data[index + 1])
    output.append(str(lca(node1, node2)))
    index += 2

sys.stdout.write("\n".join(output) + "\n")
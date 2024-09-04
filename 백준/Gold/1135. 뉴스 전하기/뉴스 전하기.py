import sys

input = sys.stdin.readline

n = int(input())
tree = [[[101, i]] for i in range(n + 1)]
parent = list(map(int, input().split()))
for i in range(1, n):
    tree[parent[i]].append([0, i])

def find_height(cur):
    for i in range(1, len(tree[cur])):
        nxt = tree[cur][i][1]
        find_height(nxt)
        tree[cur][i][0] = tree[nxt][0][0]
    
    tree[cur].sort(reverse=True)
    max_time = 0
    for i in range(1, len(tree[cur])):
        max_time = max(max_time, tree[cur][i][0] + i)
    tree[cur][0][0] = max_time
    return max_time

find_height(0)
for i in range(n):
    tree[i].sort(reverse=True)

print(tree[0][0][0])
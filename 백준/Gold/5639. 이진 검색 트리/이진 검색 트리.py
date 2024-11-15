import sys
sys.setrecursionlimit(10**4)
class Node:
    def __init__(self, val):
        self.val = val
        self.parent = -1
        self.left = -1
        self.right = -1

pre_order = list(map(int, sys.stdin.readlines()))
n = len(pre_order)
tree = [Node(0) for _ in range(n)]
tree[0].val = pre_order[0]
last = 1

def insert(val):
    global last
    cur = 0
    while True:
        if val < tree[cur].val:
            if tree[cur].left == -1:
                tree[cur].left = last
                tree[last].val = val
                tree[last].parent = cur
                last += 1
                break
            else:
                cur = tree[cur].left
        else:
            if tree[cur].right == -1:
                tree[cur].right = last
                tree[last].val = val
                tree[last].parent = cur
                last += 1
                break
            else:
                cur = tree[cur].right

for i in range(1, n):
    insert(pre_order[i])

def print_post(x: int):
    if tree[x].left != -1:
        print_post(tree[x].left)
    if tree[x].right != -1:
        print_post(tree[x].right)
    print(tree[x].val)

print_post(0)

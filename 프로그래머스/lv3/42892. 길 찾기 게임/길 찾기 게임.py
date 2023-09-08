import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    nodeinfo = [(x, y, i) for i, (x, y) in enumerate(nodeinfo, start=1)]
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    
    class treenode:
        def __init__(self, idx, x, y):
            self.idx = idx
            self.x = x
            self.y = y
            self.left = None
            self.right = None

    class tree:
        def __init__(self):
            self.root = None
            self.pre = []
            self.post = []

        def insert(self, node):
            self.root = self._insert(self.root, node)

        def _insert(self, root, node):
            if root is None:
                return node
            if root.x > node.x:
                root.left = self._insert(root.left, node)
            else:
                root.right = self._insert(root.right, node)
            return root

        def preorder(self):
            self._preorder(self.root)

        def _preorder(self, root):
            if root:
                self.pre.append(root.idx)
                self._preorder(root.left)
                self._preorder(root.right)

        def postorder(self):
            self._postorder(self.root)

        def _postorder(self, root):
            if root:
                self._postorder(root.left)
                self._postorder(root.right)
                self.post.append(root.idx)

    root = tree()
    for x, y, idx in nodeinfo:
        root.insert(treenode(idx, x, y))

    root.preorder()
    root.postorder()

    answer = [root.pre, root.post]
    return answer
class LockingTree:

    def __init__(self, parent: List[int]):
        cnt = len(parent)
        self.locked = [-1 for _ in range(cnt)]
        self.parent = parent
        self.parent_all = [[] for _ in range(cnt)]
        self.child_all = [[] for _ in range(cnt)]
        self.tree = [[] for _ in range(cnt)]
        for i in range(1, cnt):
            self.tree[parent[i]].append(i)
        
        q = deque([0])
        while q:
            node = q.popleft()
            for child in self.tree[node]:
                self.parent_all[child].append(node)
                self.parent_all[child] += self.parent_all[node]
                q.append(child)
                
        by_depth = [[]]
        q = deque([(0, 0)])
        while q:
            node, depth = q.popleft()
            if len(by_depth) <= depth:
                by_depth.append([])
            by_depth[depth].append(node)
            if self.tree[node]:
                for child in self.tree[node]:
                    q.append((child, depth + 1))

        for i in range(len(by_depth) - 1, -1, -1):
            for node in by_depth[i]:
                for child in self.tree[node]:
                    self.child_all[node].append(child)
                    self.child_all[node] += self.child_all[child]

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] != -1:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False
        self.locked[num] = -1
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked[num] != -1:
            return False

        locked = list(filter(lambda x: self.locked[x] != -1, self.child_all[num]))
        if not locked:
            return False
        
        unlocked = list(filter(lambda x: self.locked[x] != -1, self.parent_all[num]))
        if unlocked:
            return False
        
        for i in locked:
            self.locked[i] = -1
        self.locked[num] = user
        return True
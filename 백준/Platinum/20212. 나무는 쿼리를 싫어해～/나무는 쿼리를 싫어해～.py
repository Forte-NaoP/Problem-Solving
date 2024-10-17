import sys

input = sys.stdin.readline

class DST:
    def __init__(self):
        # node : [l_child, r_child, value, lazy]
        self.t = [[-1, -1, 0, 0] for _ in range(2)]
        self.idx = 1

    def get_or_insert(self, cur, idx):
        if self.t[cur][idx] == -1:
            self.idx += 1
            self.t.append([-1, -1, 0, 0])
            self.t[cur][idx] = self.idx
        return self.t[cur][idx]

    def propagate(self, s, e, cur):
        if cur == -1 or self.t[cur][3] == 0:
            return
        self.t[cur][2] += (e - s + 1) * self.t[cur][3]
        if s != e:
            l_idx = self.get_or_insert(cur, 0)
            self.t[l_idx][3] += self.t[cur][3]
            
            r_idx = self.get_or_insert(cur, 1)
            self.t[r_idx][3] += self.t[cur][3]
        
        self.t[cur][3] = 0
    
    def update_range(self, l, r, val):
        self.__update_range(l, r, val, 0, 1_000_000_000, 1)

    def __update_range(self, l, r, val, s, e, cur):
        self.propagate(s, e, cur)
        if cur == -1 or r < s or e < l:
            return
        if l <= s and e <= r:
            self.t[cur][3] += val
            self.propagate(s, e, cur)
            return
        
        mid = (s + e) // 2
        l_idx = self.get_or_insert(cur, 0)
        self.__update_range(l, r, val, s, mid, l_idx)

        r_idx = self.get_or_insert(cur, 1)
        self.__update_range(l, r, val, mid + 1, e, r_idx)
        
        self.t[cur][2] = self.t[l_idx][2] + self.t[r_idx][2]

    def query(self, l, r):
        return self.__query(l, r, 0, 1_000_000_000, 1)

    def __query(self, l, r, s, e, cur):
        if cur == -1 or r < s or e < l:
            return 0
        
        self.propagate(s, e, cur)

        if l <= s and e <= r:
            return self.t[cur][2]
        
        mid = (s + e) // 2
        l_idx = self.get_or_insert(cur, 0)
        l_val = self.__query(l, r, s, mid, l_idx)

        r_idx = self.get_or_insert(cur, 1)
        r_val = self.__query(l, r, mid + 1, e, r_idx)

        return l_val + r_val

tree = DST()

n = int(input())
q_list, u_list = [], []
cnt = 0
for _ in range(n):
    op, i, j, k = map(int, input().split())
    if op == 1:
        u_list.append((i, j, k))
    else:
        q_list.append((i, j, k, cnt))
        cnt += 1

q_list.sort(key=lambda x: x[2])

done = 0
ans = []
for i, j, k, c in q_list:
    while done < k:
        tree.update_range(*u_list[done])
        done += 1
    ans.append((tree.query(i, j), c))

ans.sort(key=lambda x: x[-1])
for q in ans:
    print(q[0])
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.reverse()
        nums2.reverse()

        tree = {}
        leaf = (nums1[0], nums2[0])

        child = None
        for num in nums1:
            if child:
                tree[child] = [[num, 0]]
            child = num

        child = None
        for num in nums2:
            if child:
                if tree.get(child):
                    tree[child].append([num, 0])
                else:
                    tree[child] = [[num, 0]]
            child = num

        def recur(node):
            if not tree.get(node):
                return node
            M_value = 0
            for i, (parent, value) in enumerate(tree[node]):
                if value == 0:
                    tree[node][i][1] = recur(parent)
                    tree[node][i][1] += node
                M_value = max(M_value, tree[node][i][1])
            return M_value

        recur(leaf[0])
        recur(leaf[1])

        return max(max(map(lambda x: x[1], tree[leaf[0]])), max(map(lambda x: x[1], tree[leaf[1]]))) % (10 ** 9 + 7)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        lv_sum = [0]
        q = deque()
        q.append((root, 0))

        while q:
            node, lv = q.popleft()
            if lv >= len(lv_sum):
                lv_sum.append(0)
            lv_sum[lv] += node.val
            if node.left:
                q.append((node.left, lv + 1))
            if node.right:
                q.append((node.right, lv + 1))
        
        if len(lv_sum) < k:
            return -1

        lv_sum.sort(reverse=True)
        return lv_sum[k - 1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, max_):
            if not root: return

            nonlocal res
            if root.val >= max_:
                res += 1

            max_ = max(root.val, max_)
                
            dfs(root.left, max_)
            dfs(root.right, max_)

        dfs(root, root.val)
        return res
        
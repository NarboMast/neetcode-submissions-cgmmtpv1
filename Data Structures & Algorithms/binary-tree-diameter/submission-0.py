# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root: return 0

            left_ = dfs(root.left)
            right_ = dfs(root.right)
            curr = 1 + max(left_, right_)
            res = max(left_ + right_, res)

            return curr

        dfs(root)
        return res  
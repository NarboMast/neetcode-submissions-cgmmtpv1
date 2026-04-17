# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        balanced = True

        def dfs(root):
            if not root: return 0

            nonlocal balanced

            left_ = dfs(root.left)
            right_ = dfs(root.right)

            if not (-1 <= (left_ - right_) <= 1): 
                balanced = False
                return 0

            return 1 + max(left_, right_)

        l = dfs(root.left)
        r = dfs(root.right)

        return balanced and -1 <= (l - r) <= 1
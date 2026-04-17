# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            len_ = len(q)
            right_node = None

            for i in range(len_):
                node = q.popleft()

                if node:
                    q.append(node.left)
                    q.append(node.right)
                    right_node = node
            
            if right_node: res.append(right_node.val)

        return res
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            len_ = len(queue)
            level = []

            for i in range(len_):
                temp = queue.popleft()

                if temp:
                    queue.append(temp.left)
                    queue.append(temp.right)
                    level.append(temp.val)
            
            if level: res.append(level)

        return res
        
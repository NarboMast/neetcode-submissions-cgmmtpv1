"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class TreeNode:
    def __init__(self, interval : 'Interval'):
        self.interval = interval
        self.left = None
        self.right = None

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True

        def dfs(node, interval):
            start, end = node.interval.start, node.interval.end
            in_start, in_end = interval.start, interval.end

            if end <= in_start:
                if not node.right:
                    node.right = TreeNode(interval)
                else:
                    return dfs(node.right, interval)
            elif start >= in_end:
                if not node.left:
                    node.left = TreeNode(interval)
                else:
                    return dfs(node.left, interval)
            else:
                return False

            return True

        root = TreeNode(intervals[0])

        for interval in intervals[1:]:
            if not dfs(root, interval):
                return False

        return True
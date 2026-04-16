# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = curr = ListNode()

        l1, l2 = list1, list2

        while l1 and l2:
            v1 = l1.val
            v2 = l2.val

            if v1 <= v2:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next

        curr.next = l1 or l2

        return res.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head_ = head
        dummy = ListNode()
        dummy.next = head_
        l, r = dummy, head_

        #update r to n
        while r and n > 0:
            r = r.next
            n -= 1

        while r:
            r = r.next
            l = l.next

        l.next = l.next.next

        return dummy.next
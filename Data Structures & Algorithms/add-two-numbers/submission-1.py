# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy

        reminder = 0
        while l1 and l2:
            sum_ = l1.val + l2.val + reminder

            digit = sum_ % 10
            reminder = sum_ // 10

            res.next = ListNode(digit)
            l1 = l1.next
            l2 = l2.next
            res = res.next

        while l1:
            sum_ = l1.val + reminder

            digit = sum_ % 10
            reminder = sum_ // 10

            res.next = ListNode(digit)
            l1 = l1.next
            res = res.next

        while l2:
            sum_ = l2.val + reminder

            digit = sum_ % 10
            reminder = sum_ // 10

            res.next = ListNode(digit)
            l2 = l2.next
            res = res.next

        if reminder != 0: res.next = ListNode(reminder)

        return dummy.next
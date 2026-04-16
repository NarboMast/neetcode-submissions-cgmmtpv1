# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #check for at least two nodes

        #find median
        s, f = head, head.next #might not contain [1]

        while f and f.next:
            s = s.next
            f = f.next.next

        second = s.next
        s.next = None
        rev = None
        #reverse from s.next
        while second:
            temp = second.next
            second.next = rev
            rev = second
            second = temp

        while head and rev:
            head_next = head.next
            rev_next = rev.next

            head.next = rev
            rev.next = head_next

            head = head_next
            rev = rev_next

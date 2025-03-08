# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = current = ListNode(0)

        while l1 or l2:
            if l1:
                current.val += l1.val
                l1 = l1.next
            if l2:
                current.val += l2.val
                l2 = l2.next

            # decide on next result digit
            if current.val >= 10:
                current.val = current.val - 10
                current.next = ListNode(1)
            elif l1 or l2:
                current.next = ListNode(0)
            current = current.next

        return result

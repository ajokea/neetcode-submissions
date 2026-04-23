# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = result = ListNode()

        carry = 0
        while l1 or l2 or carry:
            initialSum = 0
            if l1:
                initialSum += l1.val
                l1 = l1.next
            if l2:
                initialSum += l2.val
                l2 = l2.next
            if carry:
                initialSum += carry
            
            digit = initialSum % 10
            carry = initialSum // 10

            result.next = ListNode(val = digit)
            result = result.next

        return dummy.next
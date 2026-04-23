# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # get second n steps ahead of first
        first, second = dummy, head
        for _ in range(n):
            second = second.next
        
        # get first to tail - n, the node before the nth from the end
        while second:
            first = first.next
            second = second.next
        
        # remove nth node
        first.next = first.next.next

        return dummy.next
        
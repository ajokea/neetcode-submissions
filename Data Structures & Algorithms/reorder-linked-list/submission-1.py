# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle of list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is at middle - 1, so remove slow.next pointer
        curr = slow.next
        prev = slow.next = None

        # reverse second half of the list
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # reorder list
        first, second = head, prev
        while second:
            temp, temp2 = first.next, second.next
            first.next = second
            second.next = temp
            first = temp
            second = temp2
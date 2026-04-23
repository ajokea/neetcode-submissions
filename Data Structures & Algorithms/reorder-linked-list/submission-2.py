# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle of list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow points to middle of list
        curr = slow.next
        prev = slow.next = None # remove slow.next pointer to prevent cycle
        
        # reverse second half of the list
        while curr:
            temp = curr.next
            
            curr.next = prev
            prev = curr
            curr = temp

        # prev points to tail node
        first, second = head, prev
        # reorder list
        while second:
            temp = first.next
            temp2 = second.next

            first.next = second
            second.next = temp
            first = temp
            second = temp2

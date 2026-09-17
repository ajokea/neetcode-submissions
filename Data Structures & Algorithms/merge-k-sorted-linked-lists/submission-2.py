# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        n = len(lists)
        mid = n // 2
        left = self.mergeKLists(lists[0:mid])
        right = self.mergeKLists(lists[mid:n])


        current = dummy = ListNode()
        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        while left:
            current.next = left
            left = left.next
            current = current.next
        
        while right:
            current.next = right
            right = right.next
            current = current.next

        return dummy.next

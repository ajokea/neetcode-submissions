# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1

        def reverseKNodes(i, node):
            if (i + k) > n:
                return node
            
            curr, prev = node, None
            for j in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            node.next = reverseKNodes(i + k, curr)
            return prev

        return reverseKNodes(0, head)
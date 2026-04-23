# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def getHeight(node):
            if not node:
                return 0

            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            if not (abs(getHeight(curr.left) - getHeight(curr.right)) <= 1):
                return False
            stack.append(curr.left)
            stack.append(curr.right)
        return True
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [[p, q]]

        while stack:
            pNode, qNode = stack.pop()
            if not pNode and not qNode:
                continue
            elif (not pNode or not qNode) or (pNode.val != qNode.val):
                return False
            else:
                stack.append([pNode.left, qNode.left])
                stack.append([pNode.right, qNode.right])
        
        return True
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, leftLimit, rightLimit):
            if not root:
                return True

            if leftLimit < root.val < rightLimit:
                return validate(root.left, leftLimit, root.val) and validate(root.right, root.val, rightLimit)
            return False
        
        return validate(root, float('-inf'), float('inf'))
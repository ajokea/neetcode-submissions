# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def preorder(root):
            if not root:
                return
            
            if preorder(root.left):
                result.append(preorder(root.left))
            result.append(root.val)
            if preorder(root.right):
                result.append(preorder(root.right))
        
        preorder(root)

        return result[k-1]
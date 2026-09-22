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

        return abs(self.getTreeHeight(root.left) - self.getTreeHeight(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def getTreeHeight(self, root):
        if not root:
            return 0

        return 1 + max(
            self.getTreeHeight(root.left),
            self.getTreeHeight(root.right))
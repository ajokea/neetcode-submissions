# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # diameter of tree starting at current node
            self.diameter = max(self.diameter, left + right)

            # returns the height of the tree
            return 1 + max(left, right)

        dfs(root)
        return self.diameter
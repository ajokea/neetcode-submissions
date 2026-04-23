# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val

        def dfs(node):
            if not node:
                return 0
            
            leftSubtree = max(dfs(node.left), 0)
            rightSubtree = max(dfs(node.right), 0)

            # compute max sum w/ splitting
            self.result = max(self.result, node.val + leftSubtree + rightSubtree)

            # return max sum w/o splitting
            return node.val + max(leftSubtree, rightSubtree)

        dfs(root)
        return self.result
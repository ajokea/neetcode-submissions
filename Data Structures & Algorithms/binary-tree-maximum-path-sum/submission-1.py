# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]

        # to split or not to split
        def dfs(root):
            if not root:
                return 0
            
            leftTree = max(dfs(root.left), 0)
            rightTree = max(dfs(root.right), 0)

            # compute sum of path with split
            result[0] = max(result[0], root.val + leftTree + rightTree)

            # return sum of path without split
            return root.val + max(leftTree, rightTree)
        
        dfs(root)
        return result[0]
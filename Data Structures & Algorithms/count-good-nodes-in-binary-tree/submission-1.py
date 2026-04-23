# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''good: path from root to x contains no nodes 
        w/ val greater than x.val'''

        ''' traverse the tree: dfs? and keep a set of visited
        nodes to compare, then make sure x.val is the max val'''
        def dfs(node, maxVal):
            if not node:
                return 0
            
            result = 1 if node.val >= maxVal else 0
            result += dfs(node.left, max(maxVal, node.val))
            result += dfs(node.right, max(maxVal, node.val))

            return result

        return dfs(root, root.val)
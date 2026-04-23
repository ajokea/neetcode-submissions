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

        self.good = 0

        def dfs(node, path):
            if not node:
                return
            
            path.append(node.val)
            if node.val == max(path):
                self.good += 1

            dfs(node.left, path)
            dfs(node.right, path)
            
            path.pop()

        dfs(root, [])
        return self.good
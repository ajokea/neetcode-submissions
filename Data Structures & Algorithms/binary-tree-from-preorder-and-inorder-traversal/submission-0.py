# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0]) # root/subroot is always at the first index of preorder list/sublist
        idx = inorder.index(preorder[0]) # find the index of the root in the inorder list, left of it will be left subtree, right of it will be right subtree

        # b/c idx is the index of root, idx == the number of items in the left subtree, which we can use for preorder sublists
        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return root
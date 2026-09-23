# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if root:
            queue = deque([root])

            while len(queue):
                view = None
                for _ in range(len(queue)):
                    current = queue.popleft()
                    view = current.val
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
                result.append(view)

        return result
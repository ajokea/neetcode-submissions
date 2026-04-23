"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = {}

        def dfs(root):
            if root in nodeMap:
                return nodeMap[root]

            node = Node(root.val)
            nodeMap[root] = node
            for n in root.neighbors:
                node.neighbors.append(dfs(n))
            
            return node

        return dfs(node) if node else None
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(src):
            if src in visited:
                return visited[src]
            
            visited[src] = Node(src.val)
            for neighbor in src.neighbors:
                visited[src].neighbors.append(dfs(neighbor))

            return visited[src]

        return dfs(node) if node else None
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = {i: [] for i in range(n)}
        for e in edges:
            adjMap[e[0]].append(e[1])
            adjMap[e[1]].append(e[0])

        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for a in adjMap[node]:
                if a == prev:
                    continue
                if not dfs(a, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n

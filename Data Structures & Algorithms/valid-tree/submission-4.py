class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}

        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for n in graph[node]:
                if n == prev:
                    continue
                if not dfs(n, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connected = 0

        adjMap = {i:[] for i in range(n)}
        for e in edges:
            adjMap[e[0]].append(e[1])
            adjMap[e[1]].append(e[0])

        visited = set()
        def dfs(node):
            visited.add(node)

            for a in adjMap[node]:
                if a not in visited:
                    dfs(a)

        for node in adjMap:
            if node not in visited:
                dfs(node)
                connected += 1

        return connected
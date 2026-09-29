class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        for a,b in prerequisites:
            adj_list[a].append(b)

        visited = set()
        def dfs(node):
            if node in visited:
                return False

            if adj_list[node] == []:
                return True

            visited.add(node)
            for course in adj_list[node]:
                if not dfs(course):
                    return False
            visited.remove(node)
            adj_list[node] = []
            return True

        for course in adj_list:
            if not dfs(course):
                return False
        return True
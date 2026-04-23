class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            courseMap[course].append(prereq)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False

            if not courseMap[course]:
                return True

            visited.add(course)
            for prereq in courseMap[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            
            courseMap[course] = []
            return True

        for course in courseMap:
            if not dfs(course):
                return False
        return True
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereqs[course].append(pre)
        
        path = set()
        def dfs(course):
            if course in path:
                return False
            
            if not prereqs[course]:
                return True
            
            path.add(course)
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False
            path.remove(course)
            return True
        
        for course in prereqs:
            if not dfs(course):
                return False
        return True
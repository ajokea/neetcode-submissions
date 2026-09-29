class Graph:
    
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adj_list and dst in self.adj_list[src]:
            self.adj_list[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        queue = deque()
        visited = set()
        queue.append(src)
        visited.add(src)

        while queue:
            vertex = queue.popleft()
            if vertex == dst:
                return True

            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return False

        # def dfs(vertex, visited):
        #     if vertex == dst:
        #         return True

        #     visited.add(vertex)
        #     for neighbor in self.adj_list[vertex]:
        #         if neighbor not in visited:
        #             if dfs(neighbor, visited):
        #                 return True
        #     visited.remove(vertex)
        #     return False

        # return dfs(src, set())

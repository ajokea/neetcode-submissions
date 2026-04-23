class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows = len(grid)
        columns = len(grid[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(coord):
            visited.add(coord)
            for d in directions:
                newCoord = (coord[0] + d[0], coord[1] + d[1])
                if (
                    newCoord[0] in range(rows) 
                    and newCoord[1] in range(columns) 
                    and grid[newCoord[0]][newCoord[1]] == '1' 
                    and newCoord not in visited
                    ):
                    dfs(newCoord)

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs((r, c))
                    islands += 1

        return islands
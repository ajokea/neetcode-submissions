class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid),len(grid[0])
        visited = set()

        islands = 0

        def dfs(r, c):
            if (
                r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == "0" or
                (r, c) in visited):
                return

            visited.add((r, c))

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1
        
        return islands
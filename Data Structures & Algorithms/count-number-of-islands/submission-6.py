class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            # reached invalid cell
            out_of_bounds = r not in range(ROWS) or c not in range(COLS)
            if out_of_bounds or grid[r][c] == "0" or (r, c) in visited:
                return

            # explore neighbors
            visited.add((r, c))
            
            dfs(r - 1, c) # up
            dfs(r + 1, c) # down
            dfs(r, c - 1) # left
            dfs(r, c + 1) # right

            
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    islands += 1

        return islands
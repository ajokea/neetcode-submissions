class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if ((r, c) in visited or
                r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == '0'):
                return
            
            visited.add((r, c))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for row in range(rows):
            for col in range(cols):
                if (grid[row][col] == "1" and
                    (row, col) not in visited):
                    dfs(row, col)
                    islands += 1
        
        return islands

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            # reached an invalid cell: out of bounds, water, or visited
            out_of_bounds = r < 0 or c < 0 or r == ROWS or c == COLS
            if out_of_bounds or grid[r][c] == 0 or (r, c) in visited:
                return 0

            # explore neighbors
            visited.add((r, c))
            area = 1

            area += dfs(r - 1, c) # up
            area += dfs(r + 1, c) # down
            area += dfs(r, c - 1) # left
            area += dfs(r, c + 1) # right

            return area

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = max(max_area, dfs(row, col))

        return max_area
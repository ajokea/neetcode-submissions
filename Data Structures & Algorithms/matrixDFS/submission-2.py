class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def isOutOfBounds(r, c):
            return r < 0 or c < 0 or r == ROWS or c == COLS

        def dfs(r, c, visited):
            # reached invalid cell: out of bounds, visited, rock (1)
            if isOutOfBounds(r, c) or (r, c) in visited or grid[r][c] == 1:
                return 0

            # reached the bottom right corner
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            # explore other paths
            visited.add((r, c))
            
            count = 0
            count += dfs(r - 1, c, visited) # up
            count += dfs(r + 1, c, visited) # down
            count += dfs(r, c - 1, visited) # left
            count += dfs(r, c + 1, visited) # right

            # backtrack
            visited.remove((r, c))
            return count

        return dfs(0, 0, set())

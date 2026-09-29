class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        visited.add((0, 0))
        queue.append((0, 0))

        directions = [
            (-1, 0), # up
            (1, 0), # down
            (0, -1), # left
            (0, 1), # right
            (1, 1), # diagonal down, right
            (-1, -1), # diagonal up, left
            (1, -1), # diagonal down, left
            (-1, 1) # diagonal up, right
        ]

        length = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                for dr, dc in directions:
                    r2, c2 = r + dr, c + dc
                    out_of_bounds = r2 < 0 or c2 < 0 or r2 == ROWS or c2 == COLS
                    # invalid coord
                    if out_of_bounds or grid[r2][c2] == 1 or (r2, c2) in visited:
                        continue

                    queue.append((r2, c2))
                    visited.add((r2, c2))
            length += 1

        return -1
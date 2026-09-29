class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        fresh_fruits = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_fruits += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right

        minutes = 0
        while queue and fresh_fruits:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    r2, c2 = r + dr, c + dc
                    out_of_bounds = r2 < 0 or c2 < 0 or r2 == ROWS or c2 == COLS
                    if not out_of_bounds and grid[r2][c2] == 1 and (r2, c2) not in visited:
                        grid[r2][c2] = 2
                        fresh_fruits -= 1
                        visited.add((r2, c2))
                        queue.append((r2, c2))

            minutes += 1

        return minutes if not fresh_fruits else -1
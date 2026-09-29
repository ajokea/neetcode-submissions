class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or grid[0][0] == 1:
            return -1 
            
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        visited.add((0, 0))
        queue.append((0, 0))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        length = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                    
                for dr, dc in directions:
                    r2, c2 = r + dr, c + dc # neighbor
                    out_of_bounds = r2 < 0 or c2 < 0 or r2 == ROWS or c2 == COLS
                    if out_of_bounds or grid[r2][c2] == 1 or (r2, c2) in visited:
                        continue

                    queue.append((r2, c2))
                    visited.add((r2, c2))
            length += 1
        
        return -1
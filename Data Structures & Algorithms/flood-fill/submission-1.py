class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image

        STARTING_COLOR = image[sr][sc]
        ROWS, COLS = len(image), len(image[0])
        visited = set()

        def dfs(r, c):
            out_of_bounds = r < 0 or c < 0 or r == ROWS or c == COLS
            # invalid pixel: out of bounds, visited, wrong color
            if out_of_bounds or (r, c) in visited or image[r][c] != STARTING_COLOR:
                return

            # change color
            image[r][c] = color

            # check neighbors
            visited.add((r, c))
            dfs(r - 1, c) # up
            dfs(r + 1, c) # down
            dfs(r, c - 1) # left
            dfs(r, c + 1) # right

        dfs(sr, sc)
        return image
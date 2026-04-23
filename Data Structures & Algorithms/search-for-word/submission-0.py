class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(row, col, i):
            if i == len(word):
                return True

            if (
                row not in range(rows) or
                col not in range(cols) or
                (row, col) in visited or
                board[row][col] != word[i]):
                return False

            visited.add((row, col))

            result = (dfs(row - 1, col, i + 1) or 
                dfs(row + 1, col, i + 1) or 
                dfs(row, col - 1, i + 1) or 
                dfs(row, col + 1, i + 1)
            )
            
            visited.remove((row, col))

            return result

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
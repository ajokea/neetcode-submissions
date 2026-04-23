class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        cols, posDiags, negDiags = set(), set(), set()
        
        board = [["." for _ in range(n)] for _ in range(n)]

        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return

            for col in range(n):
                if (
                    col in cols or
                    (row + col) in posDiags or
                    (row - col) in negDiags
                    ):
                    continue

                cols.add(col)
                posDiags.add(row + col)
                negDiags.add(row - col)

                board[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                posDiags.remove(row + col)
                negDiags.remove(row - col)

                board[row][col] = "."


        backtrack(0)
        return result
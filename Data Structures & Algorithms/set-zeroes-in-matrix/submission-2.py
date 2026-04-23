class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        rows = [False for i in range(m)]
        cols = [False for i in range(n)]

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True
        
        for r in range(m):
            if rows[r]:
                for c in range(n):
                    matrix[r][c] = 0

        for c in range(n):
            if cols[c]:
                for r in range(m):
                    matrix[r][c] = 0
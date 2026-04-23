class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = [False for i in range(len(matrix))]
        cols = [False for i in range(len(matrix[0]))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True
        
        for r in range(len(rows)):
            if rows[r]:
                for c in range(len(matrix[0])):
                    matrix[r][c] = 0

        for c in range(len(cols)):
            if cols[c]:
                for r in range(len(matrix)):
                    matrix[r][c] = 0
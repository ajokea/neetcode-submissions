class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        '''we will use the 0th row and 0th column to
        mark the rows and columns to zero out instead of 
        sepeate arrays. we will need an additional variable
        for the 0th row due to the overlap in matrix[0][0]'''

        '''loop through the matrix and set the respective 
        0th row and 0th column corresponding to the cell to 
        zero---in the case of matrix[0][0] we will set the
        boolean for the 0th row to true instead of setting
        the cell to zero to avoid overlapping '''
        rowZero = False
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        # loop through the cells without the 0th row and 0th column
        # if the cells corresponding 0th row or 0th column is zero, set it to zero
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # matrix[0][0] is reserved for the 0th column
        # if it is set to zero, zero out the corresponding rows
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # if rowZero boolean is set to True, zero out corresponding cols
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0
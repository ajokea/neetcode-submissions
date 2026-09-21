class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # rows
        n = len(matrix[0]) # columns

        l = 0
        r = m * n - 1

        while l <= r:
            mid = (l + r) // 2

            row = mid // n
            col = mid % n

            if target < matrix[row][col]:
                r = mid - 1
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                return True

        return False
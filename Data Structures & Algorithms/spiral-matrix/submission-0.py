class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        result = []

        while left < right and top < bottom:
            # get all nums in top row:
            for i in range(left, right):
                result.append(matrix[top][i])
            # move top row down
            top += 1

            # get all nums in right column
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            # move right row to the left
            right -= 1

            # re-check boundaries
            if not (left < right and top < bottom):
                break

            # get all nums in bottom row
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            # move bottom row up
            bottom -= 1

            # get all nums in left column
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            # move left row to the right
            left += 1
        
        return result
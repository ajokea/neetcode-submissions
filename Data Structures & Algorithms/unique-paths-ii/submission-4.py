class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
            
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        table = [[0 for _ in range(n)] for _ in range(m)]
        
        blocked = False
        for row in range(m):
            if obstacleGrid[row][0] != 1 and not blocked:
                table[row][0] = 1
            elif obstacleGrid[row][0] == 1:
                blocked = True
        blocked = False
        for col in range(n):
            if obstacleGrid[0][col] != 1 and not blocked:
                table[0][col] = 1
            elif obstacleGrid[0][col] == 1:
                blocked = True

        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] == 1:
                    table[row][col] = 0
                else:
                    table[row][col] = table[row - 1][col] + table[row][col - 1]

        return table[-1][-1]
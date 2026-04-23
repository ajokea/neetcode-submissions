class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                table[i][j] = table[i + 1][j] + table[i][j + 1]
        
        return table[0][0]
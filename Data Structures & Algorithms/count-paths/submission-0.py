class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[0 for _ in range(n)] for _ in range(m)]
        table[m-1][n-1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                if (i + 1) not in range(m):
                    table[i][j] = table[i][j + 1]
                elif (j + 1) not in range(n):
                    table[i][j] = table[i + 1][j]
                else:
                    table[i][j] = table[i + 1][j] + table[i][j + 1]
        
        return table[0][0]
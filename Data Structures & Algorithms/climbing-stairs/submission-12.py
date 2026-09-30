class Solution:
    def climbStairs(self, n: int) -> int:
        table = [1, 1]

        for _ in range(2, n + 1):
            table[0], table[1] = table[1], table[0] + table[1]

        return table[-1]
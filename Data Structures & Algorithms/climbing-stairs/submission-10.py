class Solution:
    def climbStairs(self, n: int) -> int:
        table = [1, 1] # 1 way to climb to the top of 0 stairs/1 stair

        for _ in range(2, n + 1):
            # table[0], table[1] = table[1], table[0] + table[1]
            table.append(table[-1] + table[-2])

        return table[-1]
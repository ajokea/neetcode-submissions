class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = n2 = 1
        for _ in range(2, n + 1):
            n1, n2 = n2, n1 + n2
        return n2
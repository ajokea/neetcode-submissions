class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        table = [0 for _ in range(n)]
        table[0] = cost[0]
        table[1] = cost[1]

        for i in range(2, n):
            table[i] = cost[i] + min(table[i - 2], table[i - 1])
        print(table)
        return min(table[-1], table[-2])
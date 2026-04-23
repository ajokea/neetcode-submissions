class Solution:
    def minCostClimbingStairs(self, cost: List[int], i=0) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])

        table = [c for c in cost]
        for i in range(2, len(cost)):
            table[i] += min(table[i - 1], table[i - 2])

        return min(table[-1], table[-2])
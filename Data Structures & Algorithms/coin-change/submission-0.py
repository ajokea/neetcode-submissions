class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [float('inf') for i in range(amount + 1)]
        table[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if (a - coin) >= 0:
                    table[a] = min(table[a], 1 + table[a - coin])
        
        return table[-1] if table[-1] != float('inf') else -1
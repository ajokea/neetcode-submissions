class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [float('inf') for _ in range(amount + 1)]
        
        table[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    table[i] = min(
                        table[i], 
                        1 + table[i - coin])
        
        return table[-1] if table[-1] != float('inf') else -1
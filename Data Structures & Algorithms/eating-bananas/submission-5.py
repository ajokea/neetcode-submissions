class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = k = max(piles)

        while low <= high:
            mid = (low + high) // 2
            
            current_speed = 0
            for pile in piles:
                current_speed += math.ceil(pile / mid)
            
            if current_speed > h:
                low = mid + 1
            else:
                high = mid - 1
                k = mid

        return k
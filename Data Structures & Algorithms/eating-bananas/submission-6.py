class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)

        low, high = 1, k
        while low <= high:
            mid = (low + high) // 2
            
            speed = 0
            for pile in piles:
                speed += math.ceil(pile / mid)
            
            if speed > h:
                # eat faster
                low = mid + 1
            else:
                # eat slower
                high = mid - 1
                k = mid

        return k
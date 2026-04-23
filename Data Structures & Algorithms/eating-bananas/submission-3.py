class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)

        l, r = 1, k
        while l <= r:
            mid = (l + r) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            print(k, mid, hours)

            if hours <= h:
                r = mid - 1
                k = min(k, mid)
            else:
                l = mid + 1
        
        return k
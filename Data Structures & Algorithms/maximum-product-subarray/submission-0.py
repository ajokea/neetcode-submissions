class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        currentMax = currentMin = 1

        for n in nums:
            temp = currentMax
            currentMax = max(n, n * currentMax, n * currentMin)
            currentMin = min(n, n * temp, n * currentMin)

            if currentMax > result:
                result = currentMax
            
        return result
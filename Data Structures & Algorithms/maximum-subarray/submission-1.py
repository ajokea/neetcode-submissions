class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]

        currentSum = 0
        for num in nums:
            currentSum += num
            result = max(result, currentSum)
            if currentSum < 0:
                currentSum = 0

        return result
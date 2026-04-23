class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectedSum = sum(i for i in range(len(nums) + 1))

        return expectedSum - sum(nums)
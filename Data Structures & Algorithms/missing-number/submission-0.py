class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(i for i in range(len(nums) + 1))

        return total - sum(nums)
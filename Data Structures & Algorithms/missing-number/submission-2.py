class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = nums[0]

        n = len(nums)
        for i in range(1, n):
            result ^= i
            result ^= nums[i]

        return result ^ n
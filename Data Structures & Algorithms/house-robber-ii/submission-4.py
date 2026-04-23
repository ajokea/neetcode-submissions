class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robHelper(nums):
            rob1 = rob2 = 0

            for num in nums:
                rob1, rob2 = rob2, max(rob2, rob1 + num)

            return rob2

        return max(
            nums[0],
            robHelper(nums[:-1]), 
            robHelper(nums[1:])
            )
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0

        for num in nums:
            rob1, rob2 = rob2, max(rob1 + num, rob2)

        return rob2
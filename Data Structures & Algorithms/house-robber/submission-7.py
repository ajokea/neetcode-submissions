class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        table = [nums[0], max(nums[0], nums[1])]

        for i in range(2, n):
            table.append(max(table[-1], nums[i] + table[-2]))

        return table[-1]
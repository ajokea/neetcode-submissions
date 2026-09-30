class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        table = [nums[0], max(nums[0], nums[1])]

        for i in range(2, n):
            # table.append(max(table[-1], nums[i] + table[-2]))
            table[0], table[1] = table[1], max(table[1], nums[i] + table[0])

        return table[-1]
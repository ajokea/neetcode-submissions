class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        table = [nums[0]]

        for i in range(1, n):
            rob_this_house = nums[i]
            if i > 1:
                rob_this_house += table[-2]

            table.append(max(table[-1], rob_this_house))

        return table[-1]
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()

        def helper(i, subset):
            if i == len(nums):
                result.append(subset[:])
                return

            subset.append(nums[i])
            helper(i + 1, subset)
            subset.pop()

            while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1, subset)

        helper(0, [])
        return result
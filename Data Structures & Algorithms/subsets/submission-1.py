class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(i, combo):
            if i == len(nums):
                result.append(combo[:])
                return

            helper(i + 1, combo)
            combo.append(nums[i])
            helper(i + 1, combo)
            combo.pop()

        helper(0, [])
        return result
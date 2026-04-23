class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()

        def helper(i, combo):
            if i == len(nums):
                result.append(combo[:])
                return
            
            combo.append(nums[i])
            helper(i + 1, combo)
            combo.pop()

            while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1, combo)

        helper(0, [])
        return result
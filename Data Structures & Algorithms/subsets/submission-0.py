class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(i, subset):
            if i == len(nums):
                result.append(subset[:])
                return
            
            helper(i + 1, subset)
            subset.append(nums[i])
            helper(i + 1, subset)
            subset.pop()

        helper(0, [])
        return result
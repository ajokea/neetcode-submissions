class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        #nums.sort()

        def helper(i, combo, currentSum):
            if currentSum == target:
                result.append(combo.copy())
                return
            
            if currentSum > target or i == len(nums):
                return

            combo.append(nums[i])
            helper(i, combo, currentSum + nums[i])
            combo.pop()
            helper(i+1, combo, currentSum)
        
        helper(0, [], 0)

        return result

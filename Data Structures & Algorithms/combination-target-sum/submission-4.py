class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def helper(i, combo, currSum):
            if i == len(nums) or currSum > target:
                return 

            if currSum == target:
                result.append(combo[:])
                return
            
            combo.append(nums[i])
            helper(i, combo, currSum + nums[i])
            combo.pop()
            helper(i + 1, combo, currSum)
            
            '''
            for j in range(i, len(nums)):
                combo.append(nums[j])
                helper(j, combo, currSum + nums[j])
                combo.pop()
            '''
        
        helper(0, [], 0)

        return result
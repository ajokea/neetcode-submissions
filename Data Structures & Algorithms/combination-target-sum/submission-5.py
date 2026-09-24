class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []

        def dfs(i, combo, current_sum):
            if current_sum == target:
                combos.append(combo.copy())
                return

            if i == len(nums) or current_sum > target:
                return
            
            combo.append(nums[i])
            dfs(i, combo, current_sum + nums[i])
            combo.pop()
            dfs(i + 1, combo, current_sum)

        dfs(0, [], 0)
        return combos
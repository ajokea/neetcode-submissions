class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()

        def helper(i, combo, currentSum):
            if currentSum == target:
                result.append(combo[:])
                return

            if currentSum > target or i == len(candidates):
                return

            combo.append(candidates[i])
            helper(i + 1, combo, currentSum + candidates[i])
            combo.pop()

            while (i + 1) < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            helper(i + 1, combo, currentSum)

        helper(0, [], 0)
        return result
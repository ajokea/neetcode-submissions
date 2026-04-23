class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]

        result = []
        perms = self.permute(nums[1:])

        for p in perms:
            for i in range(len(nums)):
                perm = p[:]
                perm.insert(i, nums[0])
                result.append(perm)

        return result
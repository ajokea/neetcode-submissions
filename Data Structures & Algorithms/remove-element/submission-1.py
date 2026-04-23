class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, k = 0, len(nums)

        while i < k:
            if nums[i] == val:
                nums[i] = nums[k - 1]
                k -= 1
            else:
                i += 1

        return k
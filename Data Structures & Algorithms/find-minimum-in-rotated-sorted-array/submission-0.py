class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        minimum = float('inf')
        while l <= r:
            m = (l + r) // 2

            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m - 1

            minimum = min(minimum, nums[m])

        return minimum
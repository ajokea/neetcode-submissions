class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            minimum = min(minimum, nums[m])

            # in left-sorted portion of the array, so every num to the right is smaller
            if nums[m] > nums[r]:
                l = m + 1
            # in right-sorted portion of the array, so we may find smaller nums to the left
            else:
                r = m - 1
        
        return minimum
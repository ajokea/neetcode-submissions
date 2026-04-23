class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            # in the left-sorted portion of the array
            if nums[m] >= nums[l]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1

            # in the right-sorted portion of the array
            else:
                if target > nums[r] or target < nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_max = global_min = nums[0]
        curr_max = curr_min = 0
        total_sum = 0

        for num in nums:
            curr_max = max(curr_max + num, num)
            global_max = max(global_max, curr_max)

            curr_min = min(curr_min + num, num)
            global_min = min(global_min, curr_min)

            total_sum += num

        return max(total_sum - global_min, global_max) if global_max > 0 else global_max
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l, r = 0, len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
            max_area = max(max_area, area)
            
        return max_area
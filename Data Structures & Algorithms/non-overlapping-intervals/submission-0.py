class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        result = 0

        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # overlapping
            if start < prevEnd:
                result += 1
                prevEnd = min(prevEnd, end)
            # non-overlapping
            else:
                prevEnd = end
        return result
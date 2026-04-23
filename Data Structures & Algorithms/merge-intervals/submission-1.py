class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            last = result[-1]

            # merging
            if intervals[i][0] <= last[1]:
                result[-1] = [
                    min(last[0], intervals[i][0]),
                    max(last[1], intervals[i][1])
                ]
            # not merging
            else:
                result.append(intervals[i])
        
        return result
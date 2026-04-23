class Solution:
    import math
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []

        minHeap = [(math.sqrt((x ** 2) + (y ** 2)), [x, y]) for x, y in points]
        heapq.heapify(minHeap)

        i = 0
        while minHeap and i < k:
            result.append(heapq.heappop(minHeap)[1])
            i += 1

        return result
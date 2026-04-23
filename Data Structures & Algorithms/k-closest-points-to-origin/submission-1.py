class Solution:
    import math
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [(math.sqrt((x ** 2) + (y ** 2)), [x, y]) for x, y in points]
        heapq.heapify(minHeap)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(minHeap)[1])

        return result
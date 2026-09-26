class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        n = 0

        for x, y in points:
            dist_squared = x ** 2 + y ** 2
            if n == k and dist_squared < max_heap[0][0]:
                heapq.heappushpop_max(max_heap, [dist_squared, x, y])
            if n < k:
                heapq.heappush_max(max_heap, [dist_squared, x, y])
                n += 1

        return [[x, y] for [d, x, y] in max_heap]
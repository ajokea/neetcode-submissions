class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances_squared = []
        for i, [x, y] in enumerate(points):
            distances_squared.append((x ** 2 + y ** 2, i))
        heapq.heapify(distances_squared)
        results = [points[heapq.heappop(distances_squared)[1]] for _ in range(k)]
        return results
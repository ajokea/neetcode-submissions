class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def partition(start, end):
            left = start
            pivot = points[end]
            pivot_dist = self.get_distance_from_origin(points[end])

            for i in range(start, end):
                if (
                    self.get_distance_from_origin(points[i]) <
                    pivot_dist):
                    points[left], points[i] = points[i], points[left]
                    left += 1
            
            points[left], points[end] = points[end], points[left]
            return left

        start, end = 0, len(points) - 1
        pivot_index = end + 1

        while pivot_index != k:
            pivot_index = partition(0, end)
            if pivot_index < k:
                start = pivot_index + 1
            else:
                end = pivot_index - 1

        return points[:k]

    # distance squared
    def get_distance_from_origin(self, point):
        return (point[0] ** 2) + (point[1] ** 2)

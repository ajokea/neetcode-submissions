class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        if len(points) == k:
            return points

        def quickSort(start, end):
            if end - start + 1 <= 1:
                return

            left = start
            pivot = points[end]

            for i in range(start, end):
                if (
                    self.get_distance_from_origin(points[i]) <
                    self.get_distance_from_origin(points[end])):
                    points[left], points[i] = points[i], points[left]
                    left += 1
            
            points[left], points[end] = points[end], points[left]
            quickSort(start, left - 1)
            quickSort(left + 1, end)

        quickSort(0, len(points) - 1)
        return points[:k]


    def get_distance_from_origin(self, point):
        return math.sqrt((point[0] ** 2) + (point[1] ** 2))

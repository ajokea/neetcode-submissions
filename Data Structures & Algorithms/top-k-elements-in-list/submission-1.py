class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        maxHeap = [[-count, num] for num, count in counts.items()]
        heapq.heapify(maxHeap)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(maxHeap)[1])

        return result
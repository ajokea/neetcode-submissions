class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x, y = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)

            if x > y:
                heapq.heappush(maxHeap, y - x)

        return -maxHeap[0] if maxHeap else 0
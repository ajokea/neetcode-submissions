class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while n > 1:
            x, y = -heapq.heappop(max_heap), -heapq.heappop(max_heap)

            if x == y:
                n -= 2
            else:
                if x < y:
                    heapq.heappush(max_heap, -(y - x))
                else:
                    heapq.heappush(max_heap, -(x - y))
                n -= 1

        return -sum(max_heap)
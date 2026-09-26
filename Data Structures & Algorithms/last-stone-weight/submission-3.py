class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        min_heap = [-stone for stone in stones]
        heapq.heapify(min_heap)
        
        while n > 1:
            x, y = heapq.heappop(min_heap), heapq.heappop(min_heap)

            if x == y:
                n -= 2
            else:
                if abs(x) < abs(y):
                    heapq.heappush(min_heap, -(abs(y) - abs(x)))
                else:
                    heapq.heappush(min_heap, -(abs(x) - abs(y)))
                n -= 1

        return -min_heap[0] if min_heap else 0
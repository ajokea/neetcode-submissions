class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            maxHeap.append(-stone)
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            print(maxHeap)
            x, y = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)

            if x < y:
                y -= x
                heapq.heappush(maxHeap, -y)
            
            if x > y:
                x -= y
                heapq.heappush(maxHeap, -x)

        return -maxHeap[0] if maxHeap else 0
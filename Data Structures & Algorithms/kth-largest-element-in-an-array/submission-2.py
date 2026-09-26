class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        n = 0
        for num in nums:
            if n == k and num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
            
            if n < k:
                heapq.heappush(min_heap, num)
                n += 1

        return min_heap[0]
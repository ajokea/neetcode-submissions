class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums, self.k = nums, k

        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        else:
            if val > self.nums[0]:
                heapq.heappop(self.nums)
                heapq.heappush(self.nums, val)
        return self.nums[0]

    
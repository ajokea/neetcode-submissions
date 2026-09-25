class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [0] # min-heap
        self.size = 0
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if self.size == self.k and val > self.heap[1]:
            self.heap[1] = val
            i = 1
            while 2 * i <= self.size:
                if 2 * i + 1 <= self.size and self.heap[2 * i + 1] < self.heap[2 * i] and val > self.heap[2 * i + 1]:
                    # switch with right child
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = val
                    i = (2 * i + 1)
                elif val > self.heap[2 * i]:
                    #switch with left child
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = val
                    i *= 2
                else:
                    break
                    
        if self.size < self.k:
            self.heap.append(val)
            self.size += 1

            i = self.size
            while i != 1 and val < self.heap[i // 2]:
                self.heap[i] = self.heap[i // 2]
                self.heap[i // 2] = val
                i //= 2

        return self.heap[1]

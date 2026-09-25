class MinHeap:
    
    def __init__(self):
        self.nums = [0]
        self.size = 0

    def push(self, val: int) -> None:
        self.size += 1
        self.nums.append(val)

        i = self.size
        while i != 1 and val < self.nums[i // 2]:
            self.nums[i] = self.nums[i // 2]
            self.nums[i // 2] = val
            i //= 2

    def percolateDown(self, i):
        while 2 * i <= self.size:
            if 2 * i + 1 <= self.size and self.nums[2 * i + 1] < self.nums[2 * i] and self.nums[i] > self.nums[2 * i + 1]:
                # switch w/ smaller right child
                temp = self.nums[i]
                self.nums[i] = self.nums[2 * i + 1]
                self.nums[2 * i + 1] = temp
                i = 2 * i + 1
            elif self.nums[i] > self.nums[2 * i]:
                # switch w/ smaller left child
                temp = self.nums[i]
                self.nums[i] = self.nums[2 * i]
                self.nums[2 * i] = temp
                i *= 2
            else:
                break

    def pop(self) -> int:
        if not self.size:
            return -1 
        elif self.size == 1:
            self.size -= 1
            return self.nums.pop()
        else:
            popped = self.nums[1]
            self.nums[1] = self.nums.pop()
            self.size -= 1
            self.percolateDown(1)
            return popped

    def top(self) -> int:
        return self.nums[1] if self.size else - 1

    def heapify(self, nums: List[int]) -> None:
        self.size = len(nums)
        self.nums = [0] + nums
        current = self.size // 2
        while current >= 1:
            self.percolateDown(current)
            current -= 1
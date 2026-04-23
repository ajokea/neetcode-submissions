class MedianFinder:

    def __init__(self):
        self.i = 0
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.i += 1

    def findMedian(self) -> float:
        self.nums.sort()
        if self.i % 2 == 0:
            return (self.nums[self.i // 2] + self.nums[self.i // 2 - 1]) / 2    
        return self.nums[self.i//2]
class MinStack:

    def __init__(self):
        self.nums = []
        self.minNums = []

    def push(self, val: int) -> None:
        self.nums.append(val)
        
        minimum = min(val, self.minNums[-1]) if self.minNums else val
        self.minNums.append(minimum)

    def pop(self) -> None:
        self.nums.pop()
        self.minNums.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.minNums[-1]

class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [-1 for i in range(capacity)]

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        return self.array[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        newArray = [-1 for i in range(self.capacity)]
        for i, num in enumerate(self.array):
            newArray[i] = num
        self.array = newArray

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
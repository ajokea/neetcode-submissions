class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = [None for _ in range(capacity)]

    def insert(self, key: int, value: int) -> None:
        index = key % self.capacity
        while True:
            if not self.map[index]:
                self.map[index] = Pair(key, value)
                self.size += 1
                if self.size * 2 == self.capacity:
                    self.resize()
                break
            elif self.map[index].key == key:
                self.map[index].value = value
                break
            else:
                index = (index + 1) % self.capacity

    def get(self, key: int) -> int:
        index = key % self.capacity
        while self.map[index]:
            if self.map[index].key == key:
                return self.map[index].value
            index = (index + 1) % self.capacity
        return -1

    def remove(self, key: int) -> bool:
        index = key % self.capacity
        while self.map[index]:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return True
            index = (index + 1) % self.capacity
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        self.size = 0
        old_map = self.map
        self.map = [None for _ in range(self.capacity)]

        for pair in old_map:
            if pair:
                self.insert(pair.key, pair.value)

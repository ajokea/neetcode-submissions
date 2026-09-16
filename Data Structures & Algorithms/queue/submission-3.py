class Node:
    def __init__(self, val = -1, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        node = Node(value, self.tail)
        if not self.tail:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

        self.size += 1

    def appendleft(self, value: int) -> None:
        node = Node(value, next = self.head)
        if not self.head:
            self.tail = node
        else:
            self.head.prev = node
        self.head = node

        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return node.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return node.val
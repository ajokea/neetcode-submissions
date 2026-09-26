class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add(self, node):
        if not self.head:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node
    
    def remove(self, node):
        if node == self.head == self.tail:
            self.head = self.tail = None
        elif node == self.head:
            self.head = self.head.next
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next

        node.prev = None
        node.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        self.cache = {}
        self.lru = LinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            if self.cache[key] != self.lru.tail:
                self.lru.remove(self.cache[key])
                self.lru.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            if self.cache[key] != self.lru.tail:
                self.lru.remove(self.cache[key])
                self.lru.add(self.cache[key])
        else:
            self.cache[key] = ListNode(key, value)
            self.lru.add(self.cache[key])
            if self.size == self.capacity:
                del self.cache[self.lru.head.key]
                self.lru.remove(self.lru.head)
            else:
                self.size += 1
        
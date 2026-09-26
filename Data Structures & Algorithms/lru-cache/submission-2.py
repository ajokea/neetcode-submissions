class ListNode:
    def __init__(self, val = -1):
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
        self.pointers = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            if self.pointers[key] != self.lru.tail:
                self.lru.remove(self.pointers[key])
                self.lru.add(self.pointers[key])
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache and self.pointers[key] != self.lru.tail:
            self.lru.remove(self.pointers[key])
            self.lru.add(self.pointers[key])
        
        if key not in self.cache:
            self.pointers[key] = ListNode(key)
            if self.size == self.capacity:
                del self.cache[self.lru.head.val]
                del self.pointers[self.lru.head.val]
                self.lru.remove(self.lru.head)
            else:
                self.size += 1
            self.lru.add(self.pointers[key])
        
        self.cache[key] = value
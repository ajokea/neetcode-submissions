class Node:

    def __init__(self, key=-1, val=-1):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # maps key to node

        self.headDummy, self.tailDummy = Node(), Node()
        self.headDummy.next = self.tailDummy
        self.tailDummy.prev = self.headDummy
    
    # add node to end of the list
    def insert(self, node):
        last = self.tailDummy.prev
        last.next = self.tailDummy.prev = node
        node.prev, node.next = last, self.tailDummy

    # remove node from list
    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove and add to end of the list
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.headDummy.next
            self.remove(self.headDummy.next)
            del self.cache[lru.key]

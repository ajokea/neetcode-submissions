class MyNode:
    def __init__(self, val = -1, next = None):
        self.val = val
        self.next = next

class MyQueue:
    def __init__(self, items = []):
        self.head = self.tail = None
        self.size = 0
        for item in items:
            self.enqueue(item)

    def enqueue(self, val):
        node = MyNode(val)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

        self.size += 1

    def dequeue(self):
        if self.head:
            node = self.head
            self.head = self.head.next
            node.next = None
            self.size -= 1
            return node

class MyStack:

    def __init__(self):
        self.queue = MyQueue()

    def push(self, x: int) -> None:
        self.queue.enqueue(x)

    def pop(self) -> int:
        for _ in range(self.queue.size - 1):
            self.push(self.queue.dequeue().val)
        return self.queue.dequeue().val

    def top(self) -> int:
        return self.queue.tail.val

    def empty(self) -> bool:
        return self.queue.head == None


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()